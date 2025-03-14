import { Table } from 'antd';
import { useState, useEffect } from 'react';
import httpClient from '../../../api/httpClient';

interface SubjectWithMarks {
  discipline_id: number;
  discipline_name: string;
  avg_mark: number;
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
      dataIndex: 'discipline_name',
      key: 'discipline_name',
    },
    {
      title: 'Средний балл',
      dataIndex: 'avg_mark',
      key: 'avg_mark',
      render: (value: number) => value.toFixed(2),
    }
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
            sortBy: 'avg_mark'
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
      rowKey="discipline_id"
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
