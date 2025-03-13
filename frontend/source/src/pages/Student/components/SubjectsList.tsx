import { Table } from 'antd';
import { useState, useEffect } from 'react';
import httpClient from '../../../api/httpClient';

interface SubjectWithMarks {
  id: number;
  name: string;
  track_id: number;
  course_number: number;
  semester_number: number;
  avg_marks: number;
}

interface SubjectsResponse {
  items: SubjectWithMarks[];
  total: number;
}

const SubjectsList = () => {
  const [subjects, setSubjects] = useState<SubjectWithMarks[]>([]);
  const [loading, setLoading] = useState(true);
  const [total, setTotal] = useState(0);

  const columns = [
    {
      title: 'Предмет',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Средний балл',
      dataIndex: 'avg_marks',
      key: 'avg_marks',
      render: (value: number) => value.toFixed(2),
    },
    {
      title: 'Курс',
      dataIndex: 'course_number',
      key: 'course_number',
    },
    {
      title: 'Семестр',
      dataIndex: 'semester_number',
      key: 'semester_number',
    },
  ];

  useEffect(() => {
    const fetchSubjectsWithMarks = async () => {
      try {
        // Получаем ID текущего пользователя
        const userResponse = await httpClient.get('/auth/jwt/me');
        const studentId = userResponse.data.id;

        // Получаем предметы со средними оценками
        const { data } = await httpClient.get<SubjectsResponse>(`/students/${studentId}/disciplines/marks-avg`, {
          params: {
            page: 1,
            perPage: 10,
            sortOrder: 'desc',
            sortBy: 'avg_marks'
          }
        });

        setSubjects(data.items);
        setTotal(data.total);
      } catch (error) {
        console.error('Error fetching subjects:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchSubjectsWithMarks();
  }, []);

  return (
    <Table 
      columns={columns} 
      dataSource={subjects} 
      rowKey="id"
      loading={loading}
      pagination={{
        total,
        pageSize: 10,
        showSizeChanger: false
      }}
    />
  );
};

export default SubjectsList;
