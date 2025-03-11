import { createBrowserRouter, Navigate } from "react-router-dom";
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

const router = createBrowserRouter([
  { path: '/', element: <Navigate to="/login" replace /> },
  { path: '/login', element: <LoginPage /> },
  { path: '/register', element: <RegisterPage /> },
  {
    path: '/student',
    element: <StudentLayout />,
    children: [
      { path: 'dashboard', element: <Dashboard /> },
      { path: 'marks', element: <Marks /> },
    ],
  },
  {
    path: '/teacher',
    element: <TeacherLayout />,
    children: [
      { path: 'dashboard', element: <TeacherDashboard /> },
      { path: 'grade-assignment', element: <GradeAssignment /> },
    ],
  },
  {
    path: '/admin',
    element: <AdminLayout />,
    children: [
      { path: 'dashboard', element: <AdminDashboard /> },
      { path: 'requests', element: <TeacherRequests /> },
      { path: 'users', element: <UserManagement /> },
      { path: 'groups', element: <CreateGroup /> },
      { path: 'disciplines', element: <CreateDiscipline /> },
    ],
  }
]);

export default router;