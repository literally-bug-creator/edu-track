// Типы для API запросов преподавателя

// GET /api/teacher/groups
export interface Group {
  id: string;
  name: string;
  courseNumber: number;
  studentsCount: number;
  averageGrade?: number;
  department: string;
}

export interface GroupsResponse {
  items: Group[];
  total: number;
}

// GET /api/teacher/students
export interface StudentListRequestParams {
  groupId: string;
}

export interface Student {
  id: string;
  fullName: string;
  email: string;
  groupId: string;
  groupName: string;
  averageGrade?: number;
  attendanceRate?: number;
}

export interface StudentsResponse {
  items: Student[];
  total: number;
}

// POST /api/teacher/grades
export interface GradeRequest {
  studentId: string;
  disciplineId: string;
  workTypeId: string;
  score: number;
  date: string;
  comment?: string;
}

export interface GradeBulkRequest {
  grades: GradeRequest[];
}

export interface GradeResponse {
  id: string;
  studentId: string;
  disciplineId: string;
  workTypeId: string;
  score: number;
  date: string;
  comment?: string;
  createdAt: string;
  updatedAt: string;
}

// GET /api/teacher/grades-distribution
export interface GradesDistributionRequest {
  disciplineId: string;
  workTypeId: string;
  groupId?: string;
  startDate?: string;
  endDate?: string;
}

export interface GradesDistribution {
  excellent: number;    // Количество "5"
  good: number;        // Количество "4"
  satisfactory: number; // Количество "3"
  unsatisfactory: number; // Количество "2"
  total: number;
  averageGrade: number;
  workTypeName: string;
  disciplineName: string;
}

// GET /api/teacher/groups-average
export interface GroupAverageRequest {
  disciplineId?: string;
  startDate?: string;
  endDate?: string;
}

export interface GroupAverage {
  groupId: string;
  groupName: string;
  averageGrade: number;
  studentsCount: number;
  excellentCount: number;
  goodCount: number;
  satisfactoryCount: number;
  unsatisfactoryCount: number;
  disciplineId?: string;
  disciplineName?: string;
}

export interface GroupsAverageResponse {
  items: GroupAverage[];
  total: number;
  overallAverage: number;
}

// GET /api/teacher/disciplines
export interface TeacherDiscipline {
  id: string;
  name: string;
  semester: number;
  groups: {
    id: string;
    name: string;
    studentsCount: number;
  }[];
  workTypes: {
    id: string;
    name: string;
    maxScore: number;
  }[];
  department: string;
}

export interface DisciplinesResponse {
  items: TeacherDiscipline[];
  total: number;
}

// Общие типы
export interface ErrorResponse {
  message: string;
  code: string;
  details?: Record<string, string>;
}
