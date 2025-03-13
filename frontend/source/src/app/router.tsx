import { createBrowserRouter, Navigate, useNavigate } from "react-router-dom";
import { isAuthenticated, validateToken, getCurrentUser } from "../api/auth";
import { useState, useEffect } from "react";
import LoginPage from "../pages/auth/LoginPage";
import RegisterPage from "../pages/auth/RegisterPage";
import Marks from "../pages/Student/Marks";
import Dashboard from "../pages/Student/Dashboard";
import StudentLayout from "../layouts/StudentLayout";
import TeacherLayout from "../layouts/TeacherLayout";
import GradeAssignment from "../pages/Teacher/GradeAssignment";
import TeacherDashboard from "../pages/Teacher/Dashboard";
import AdminLayout from "../layouts/AdminLayout";
import AdminDashboard from "../pages/Admin/Dashboard";
import TeacherRequests from "../pages/Admin/TeacherRequests";
import CreateGroup from "../pages/Admin/CreateGroup";
import CreateDiscipline from "../pages/Admin/CreateDiscipline";
import UserManagement from "../pages/Admin/UserManagement";
import CreateTrack from "../pages/Admin/CreateTrack";
import CreateUnit from "../pages/Admin/CreateUnit";

interface ProtectedRouteProps {
  children: React.ReactNode;
}

interface AdminRouteProps {
  children: React.ReactNode;
}

interface RoleRouteProps {
  children: React.ReactNode;
  allowedRole: number;
}

const ProtectedRoute = ({ children }: ProtectedRouteProps) => {
  const [isAuth, setIsAuth] = useState<boolean>(false); // изменено начальное значение на false
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        if (!isAuthenticated()) {
          setIsAuth(false);
          setLoading(false);
          return;
        }
        
        const auth = await validateToken();
        setIsAuth(auth);
      } catch {
        setIsAuth(false);
      } finally {
        setLoading(false);
      }
    };

    checkAuth();
  }, []);

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (!isAuth) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
};

const AdminRoute = ({ children }: AdminRouteProps) => {
  const [isAdmin, setIsAdmin] = useState<boolean>(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAdminAccess = async () => {
      try {
        if (!isAuthenticated()) {
          setIsAdmin(false);
          setLoading(false);
          return;
        }

        const user = await getCurrentUser();
        setIsAdmin(user.role === 0);
      } catch {
        setIsAdmin(false);
      } finally {
        setLoading(false);
      }
    };

    checkAdminAccess();
  }, []);

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (!isAdmin) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
};

const RoleRoute = ({ children, allowedRole }: RoleRouteProps) => {
  const [hasAccess, setHasAccess] = useState<boolean>(false);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const checkAccess = async () => {
      try {
        if (!isAuthenticated()) {
          setHasAccess(false);
          setLoading(false);
          return;
        }

        const user = await getCurrentUser();
        if (user.role === allowedRole) {
          setHasAccess(true);
        } else {
          // Перенаправляем пользователя на его домашнюю страницу
          switch (user.role) {
            case 0:
              navigate('/admin/dashboard', { replace: true });
              break;
            case 1:
              navigate('/teacher/dashboard', { replace: true });
              break;
            default:
              navigate('/student/dashboard', { replace: true });
          }
        }
      } catch {
        setHasAccess(false);
      } finally {
        setLoading(false);
      }
    };

    checkAccess();
  }, [allowedRole, navigate]);

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (!hasAccess) {
    return null; // Возвращаем null, так как перенаправление уже выполнено в useEffect
  }

  return <>{children}</>;
};

const AuthRedirect = ({ children }: { children: React.ReactNode }) => {
  const [isAuth, setIsAuth] = useState<boolean>(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        if (!isAuthenticated()) {
          setIsAuth(false);
          setLoading(false);
          return;
        }
        
        const auth = await validateToken();
        setIsAuth(auth);
      } catch {
        setIsAuth(false);
      } finally {
        setLoading(false);
      }
    };

    checkAuth();
  }, []);

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (isAuth) {
    // Если пользователь авторизован, перенаправляем его на соответствующую страницу
    return <Navigate to="/student/dashboard" replace />;
  }

  return <>{children}</>;
};

const router = createBrowserRouter([
  { 
    path: '/', 
    element: <Navigate to="/login" replace /> 
  },
  { 
    path: '/login', 
    element: (
      <AuthRedirect>
        <LoginPage />
      </AuthRedirect>
    ) 
  },
  { 
    path: '/register', 
    element: (
      <AuthRedirect>
        <RegisterPage />
      </AuthRedirect>
    ) 
  },
  {
    path: '/student',
    element: (
      <ProtectedRoute>
        <RoleRoute allowedRole={2}>
          <StudentLayout />
        </RoleRoute>
      </ProtectedRoute>
    ),
    children: [
      { path: 'dashboard', element: <Dashboard /> },
      { path: 'marks', element: <Marks /> },
    ],
  },
  {
    path: '/teacher',
    element: (
      <ProtectedRoute>
        <RoleRoute allowedRole={1}>
          <TeacherLayout />
        </RoleRoute>
      </ProtectedRoute>
    ),
    children: [
      { path: 'dashboard', element: <TeacherDashboard /> },
      { path: 'grade-assignment', element: <GradeAssignment /> },
    ],
  },
  {
    path: '/admin',
    element: (
      <ProtectedRoute>
        <RoleRoute allowedRole={0}>
          <AdminLayout />
        </RoleRoute>
      </ProtectedRoute>
    ),
    children: [
      { path: 'dashboard', element: <AdminDashboard /> },
      { path: 'requests', element: <TeacherRequests /> },
      { path: 'users', element: <UserManagement /> },
      { path: 'groups', element: <CreateGroup /> },
      { path: 'disciplines', element: <CreateDiscipline /> },
      { path: 'tracks', element: <CreateTrack /> },
      { path: 'units', element: <CreateUnit /> },
    ],
  }
]);

export default router;