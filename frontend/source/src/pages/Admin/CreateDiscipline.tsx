import { Card, Form, Input, Select, Button, Table, message } from 'antd';
import { useState, useEffect } from 'react';
import type { TableColumnsType, TablePaginationConfig } from 'antd';
import httpClient from '../../api/httpClient';

interface Unit {
  id: number;
  name: string;
}

interface Discipline {
  id: number;
  name: string;
  track_id: number;
  course_number: number;
  semester_number: number;
}

interface PaginatedResponse<T> {
  items: T[];
  total: number;
}

interface CreateDisciplineRequest {
  name: string;
  track_id: number;
  course_number: number;
  semester_number: number;
}

const CreateDiscipline = () => {
  const [units, setUnits] = useState<Unit[]>([]);
  const [disciplines, setDisciplines] = useState<Discipline[]>([]);
  const [loading, setLoading] = useState(false);
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 10,
    total: 0
  });

  const [form] = Form.useForm();
  const [availableSemesters, setAvailableSemesters] = useState<number[]>([]);

  const fetchDisciplines = async (
    page: number = 1,
    perPage: number = 10,
    sortBy?: string,
    sortOrder?: string
  ) => {
    try {
      setLoading(true);
      const params = new URLSearchParams({
        page: String(page),
        perPage: String(perPage),
        ...(sortBy && { sortBy }),
        ...(sortOrder && { sortOrder })
      });

      const { data } = await httpClient.get(`/disciplines?${params}`);
      setDisciplines(data.items);
      setPagination(prev => ({ ...prev, total: data.total }));
    } catch (error) {
      message.error('Ошибка при загрузке дисциплин');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const loadInitialData = async () => {
      try {
        // Загрузка подразделений
        const { data } = await httpClient.get('/units');
        setUnits(data.items);
        
        // Загрузка дисциплин
        fetchDisciplines();
      } catch (error) {
        message.error('Ошибка при загрузке данных');
      }
    };

    loadInitialData();
  }, []);

  const handleTableChange = (pagination: TablePaginationConfig, filters: any, sorter: any) => {
    fetchDisciplines(
      pagination.current,
      pagination.pageSize,
      sorter.field,
      sorter.order
    );
  };

  const disciplineColumns: TableColumnsType<Discipline> = [
    { 
      title: 'Название',
      dataIndex: 'name',
      sorter: true
    },
    {
      title: 'Курс',
      dataIndex: 'course_number',
      sorter: true
    },
    {
      title: 'Семестр',
      dataIndex: 'semester_number',
      sorter: true
    }
  ];

  const courseNumbers = [1, 2, 3, 4];
  const semesterNumbers = [1, 2];

  // Функция для обновления доступных семестров при выборе курса
  const updateAvailableSemesters = (courseNumber: number) => {
    setAvailableSemesters([1, 2]);
    // Сбрасываем выбранный семестр если он не входит в новый диапазон
    form.setFieldValue('semester_number', undefined);
  };

  const onFinish = async (values: any) => {
    try {
      await httpClient.put('/disciplines', values);
      message.success('Дисциплина успешно создана');
      form.resetFields();
      fetchDisciplines(); // Обновляем список после создания
    } catch (error) {
      message.error('Ошибка при создании дисциплины');
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <Card title="Создание дисциплины">
        <Form form={form} layout="vertical" onFinish={onFinish}>
          <Form.Item
            label="Название дисциплины"
            name="name"
            rules={[{ required: true, message: 'Введите название дисциплины' }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Подразделение"
            name="track_id"
            rules={[{ required: true, message: 'Выберите подразделение' }]}
          >
            <Select placeholder="Выберите подразделение">
              {units.map(unit => (
                <Select.Option key={unit.id} value={unit.id}>
                  {unit.name}
                </Select.Option>
              ))}
            </Select>
          </Form.Item>

          <Form.Item
            label="Номер курса"
            name="course_number"
            rules={[{ required: true, message: 'Выберите номер курса' }]}
          >
            <Select 
              placeholder="Выберите номер курса"
              onChange={(value) => updateAvailableSemesters(value)}
            >
              {courseNumbers.map(num => (
                <Select.Option key={num} value={num}>
                  {num} курс
                </Select.Option>
              ))}
            </Select>
          </Form.Item>

          <Form.Item
            label="Номер семестра"
            name="semester_number"
            rules={[{ required: true, message: 'Выберите номер семестра' }]}
          >
            <Select placeholder="Выберите номер семестра">
              {availableSemesters.map(num => (
                <Select.Option key={num} value={num}>
                  {num} семестр
                </Select.Option>
              ))}
            </Select>
          </Form.Item>

          <Form.Item>
            <Button type="primary" htmlType="submit">
              Создать
            </Button>
          </Form.Item>
        </Form>
      </Card>

      <Card title="Список дисциплин" style={{ marginTop: 16 }}>
        <Table
          columns={disciplineColumns}
          dataSource={disciplines}
          rowKey="id"
          pagination={pagination}
          onChange={handleTableChange}
          loading={loading}
        />
      </Card>
    </div>
  );
};

export default CreateDiscipline;
