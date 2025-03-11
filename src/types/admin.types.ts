// User Management Types
export interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  middleName?: string;
  role: 'student' | 'teacher' | 'admin' | null;
  createdAt: string;
  updatedAt: string;
}

export interface UsersResponse {
  items: User[];
  total: number;
}

export interface ChangeRoleRequest {
  role: 'student' | 'teacher' | 'admin';
}

export interface TeacherRequest {
  id: string;
  firstName: string;
  lastName: string;
  middleName?: string;
  email: string;
  department: string;
  status: 'pending' | 'approved' | 'rejected';
  createdAt: string;
  comment?: string;
}

export interface TeacherRequestsResponse {
  items: TeacherRequest[];
  total: number;
}

// Group Management Types
export interface CreateGroupRequest {
  name: string;
  departmentId: string;
  courseNumber: number;
  studentIds: string[];
}

export interface Group {
  id: string;
  name: string;
  departmentId: string;
  departmentName: string;
  courseNumber: number;
  studentsCount: number;
  createdAt: string;
  updatedAt: string;
}

export interface GroupsResponse {
  items: Group[];
  total: number;
}

export interface Department {
  id: string;
  name: string;
  faculty: string;
}

export interface DepartmentsResponse {
  items: Department[];
  total: number;
}

export interface StudentForGroup {
  id: string;
  firstName: string;
  lastName: string;
  middleName?: string;
  email: string;
  groupId?: string;
  groupName?: string;
}

export interface StudentsResponse {
  items: StudentForGroup[];
  total: number;
}

// Discipline Management Types
export interface CreateDisciplineRequest {
  name: string;
  departmentId: string;
  semester: number;
  teacherIds: string[];
  groupIds: string[];
  workTypes: {
    name: string;
    maxScore: number;
  }[];
}

export interface Discipline {
  id: string;
  name: string;
  departmentId: string;
  departmentName: string;
  semester: number;
  teachers: {
    id: string;
    name: string;
  }[];
  groups: {
    id: string;
    name: string;
  }[];
  workTypes: {
    id: string;
    name: string;
    maxScore: number;
  }[];
  createdAt: string;
  updatedAt: string;
}

export interface DisciplinesResponse {
  items: Discipline[];
  total: number;
}

export interface TeacherForDiscipline {
  id: string;
  firstName: string;
  lastName: string;
  middleName?: string;
  department: string;
  disciplines: string[];
}

export interface TeachersResponse {
  items: TeacherForDiscipline[];
  total: number;
}

// Analytics Types
export interface PerformanceAnalytics {
  overallAverageGrade: number;
  gradeDistribution: {
    excellent: number;
    good: number;
    satisfactory: number;
    unsatisfactory: number;
  };
  trendByMonth: Array<{
    month: string;
    averageGrade: number;
    studentsCount: number;
  }>;
  byDepartment: Array<{
    departmentName: string;
    averageGrade: number;
    studentsCount: number;
  }>;
}

export interface TeacherAnalytics {
  items: Array<{
    teacherId: string;
    teacherName: string;
    department: string;
    disciplinesCount: number;
    studentsCount: number;
    averageGrade: number;
    gradeDistribution: {
      excellent: number;
      good: number;
      satisfactory: number;
      unsatisfactory: number;
    };
  }>;
  total: number;
}

export interface GroupAnalytics {
  items: Array<{
    groupId: string;
    groupName: string;
    department: string;
    courseNumber: number;
    studentsCount: number;
    averageGrade: number;
    attendanceRate: number;
    gradeDistribution: {
      excellent: number;
      good: number;
      satisfactory: number;
      unsatisfactory: number;
    };
  }>;
  total: number;
}

// Common Types
export interface ErrorResponse {
  message: string;
  code: string;
  details?: Record<string, string>;
}
