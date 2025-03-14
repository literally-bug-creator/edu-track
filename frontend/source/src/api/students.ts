import httpClient from './httpClient';

export interface Student {
  id: number;
  first_name: string;
  middle_name: string;
  last_name: string;
  group_id: number | null;
}

export interface StudentUpdate {
  first_name?: string;
  middle_name?: string;
  last_name?: string;
  group_id?: number;
}

interface GroupResponse {
  id: number;
  number: string;  // Изменил name на number
  track_id: number;
}

interface ApiResponse<T> {
  items: T[];
  total: number;
}

export const getStudents = () => {
  return httpClient.get<ApiResponse<Student>>('/students');
};

export const updateStudent = (id: number, data: StudentUpdate) => {
  return httpClient.patch<Student>(`/students/${id}`, data);
};

export const getGroups = () => {
  return httpClient.get<ApiResponse<GroupResponse>>('/groups');
};
