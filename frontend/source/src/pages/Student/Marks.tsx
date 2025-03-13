import { useState, useEffect } from 'react';
import { Select, Table, Card, message } from 'antd';
import type { TableColumnsType, TablePaginationConfig } from 'antd';
import type { SorterResult } from 'antd/es/table/interface';
import httpClient from '../../api/httpClient';

interface Discipline {
  id: number;
  name: string;
}

interface Mark {
  discipline_id: number;
  student_id: number;
  work_type: number;
  type: number;
  date: string;
}

interface MarksParams {
  student_id: number;
  page: number;
  perPage: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
  discipline_id?: number;
  work_type?: number;
}

interface DisciplinesParams {
  page: number;
  perPage: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
}

const Marks = () => {
  const [selectedDiscipline, setSelectedDiscipline] = useState<number>();
  const [selectedWorkType, setSelectedWorkType] = useState<number>();
  const [marks, setMarks] = useState<Mark[]>([]);
  const [disciplines, setDisciplines] = useState<Discipline[]>([]);
  const [loading, setLoading] = useState(false);
  const [total, setTotal] = useState(0);
  const [params, setParams] = useState<MarksParams>({
    student_id: 0,
    page: 1,
    perPage: 10,
    sortOrder: 'asc'
  });

  useEffect(() => {
    const getCurrentStudent = async () => {
      try {
        const { data } = await httpClient.get('/auth/jwt/me');
        setParams(prev => ({
          ...prev,
          student_id: data.id
        }));

        // После получения ID студента, загружаем его дисциплины
        const disciplinesResponse = await httpClient.get(`/students/${data.id}/disciplines`, {
          params: {
            page: 1,
            perPage: 100, // Загружаем все дисциплины сразу
            sortOrder: 'asc'
          }
        });
        
        setDisciplines(disciplinesResponse.data.items);
      } catch (error) {
        message.error('Ошибка при получении данных пользователя');
      }
    };

    getCurrentStudent();
  }, []);

  const workTypes = [
    { value: 'homework', label: 'Домашняя работа' },
    { value: 'test', label: 'Тест' },
    { value: 'exam', label: 'Экзамен' },
  ];

  const columns: TableColumnsType<Mark> = [
    {
      title: 'Тип работы',
      dataIndex: 'work_type',
      key: 'work_type',
    },
    {
      title: 'Оценка',
      dataIndex: 'type',
      key: 'type',
    },
    {
      title: 'Дата',
      dataIndex: 'date',
      key: 'date',
      render: (date: string) => new Date(date).toLocaleDateString('ru-RU')
    },
  ];

  const fetchMarks = async (parameters: MarksParams) => {
    setLoading(true);
    try {
      const { data } = await httpClient.get(`/students/${parameters.student_id}/marks`, {
        params: {
          page: parameters.page,
          perPage: parameters.perPage,
          sortBy: parameters.sortBy,
          sortOrder: parameters.sortOrder,
          discipline_id: parameters.discipline_id,
          work_type: parameters.work_type
        }
      });
      setMarks(data.items);
      setTotal(data.total);
    } catch (error) {
      message.error('Ошибка при загрузке оценок');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (params.student_id !== 0) { // Запрашиваем оценки только если получили ID студента
      fetchMarks(params);
    }
  }, [params]);

  const handleTableChange = (
    pagination: TablePaginationConfig,
    _: any,
    sorter: SorterResult<Mark>
  ) => {
    setParams({
      ...params,
      page: pagination.current || 1,
      perPage: pagination.pageSize || 10,
      sortBy: sorter.field as string,
      sortOrder: sorter.order === 'descend' ? 'desc' : 'asc'
    });
  };

  const handleDisciplineChange = (value: number) => {
    setSelectedDiscipline(value);
    setParams({
      ...params,
      discipline_id: value,
      page: 1 // Сброс на первую страницу при изменении фильтра
    });
  };

  const handleWorkTypeChange = (value: number) => {
    setSelectedWorkType(value);
    setParams({
      ...params,
      work_type: value,
      page: 1 // Сброс на первую страницу при изменении фильтра
    });
  };

  return (
    <Card title="Мои оценки" style={{ margin: 20 }}>
      <div style={{ display: 'flex', gap: 16, marginBottom: 20 }}>
        <Select
          style={{ width: 200 }}
          placeholder="Выберите дисциплину"
          options={disciplines.map(d => ({ value: d.id, label: d.name }))}
          value={selectedDiscipline}
          onChange={handleDisciplineChange}
        />
        <Select
          style={{ width: 200 }}
          placeholder="Выберите тип работы"
          options={workTypes}
          value={selectedWorkType}
          onChange={handleWorkTypeChange}
        />
      </div>
      <Table
        columns={columns}
        dataSource={marks}
        rowKey="id"
        loading={loading}
        onChange={handleTableChange}
        pagination={{
          current: params.page,
          pageSize: params.perPage,
          total: total,
          showSizeChanger: true,
          showTotal: (total) => `Всего ${total} записей`
        }}
      />
    </Card>
  );
};

export default Marks;
