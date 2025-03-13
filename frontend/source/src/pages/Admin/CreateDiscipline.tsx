import { Card, Form, Input, Select, Button, Table, message } from 'antd';
import { useState, useEffect } from 'react';
import type { TableColumnsType } from 'antd';
import httpClient from '../../api/httpClient';

interface Teacher {
  id: string;
  name: string;
  department: string;
}

interface Group {
  id: string;
  name: string;
  course: string;
}

const CreateDiscipline = () => {
  const [selectedTeachers, setSelectedTeachers] = useState<string[]>([]);
  const [selectedGroups, setSelectedGroups] = useState<string[]>([]);
  const [teachers, setTeachers] = useState<Teacher[]>([]);
  const [groups, setGroups] = useState<Group[]>([]);
  const [loading, setLoading] = useState(false);
  const [form] = Form.useForm();

  const teacherColumns: TableColumnsType<Teacher> = [
    { title: 'ФИО', dataIndex: 'name', key: 'name' },
    { title: 'Кафедра', dataIndex: 'department', key: 'department' },
  ];

  const groupColumns: TableColumnsType<Group> = [
    { title: 'Название группы', dataIndex: 'name', key: 'name' },
    { title: 'Курс', dataIndex: 'course', key: 'course' },
  ];

  useEffect(() => {
    const fetchTeachers = async () => {
      try {
        const { data } = await httpClient.get('/teachers');
        setTeachers(data);
      } catch (error) {
        console.error('Error fetching teachers:', error);
        message.error('Ошибка при загрузке списка преподавателей');
      }
    };

    const fetchGroups = async () => {
      try {
        const { data } = await httpClient.get('/groups');
        setGroups(data);
      } catch (error) {
        console.error('Error fetching groups:', error);
        message.error('Ошибка при загрузке списка групп');
      }
    };

    fetchTeachers();
    fetchGroups();
  }, []);

  const handleSubmit = async (values: any) => {
    setLoading(true);
    try {
      const disciplineData = {
        ...values,
        teachers: selectedTeachers,
        groups: selectedGroups,
      };

      await httpClient.post('/api/disciplines', disciplineData);
      
      message.success('Дисциплина успешно создана');
      form.resetFields();
      setSelectedTeachers([]);
      setSelectedGroups([]);
    } catch (error) {
      console.error('Error creating discipline:', error);
      message.error('Ошибка при создании дисциплины');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <Card title="Создание новой дисциплины">
        <Form
          form={form}
          layout="vertical"
          onFinish={handleSubmit}
        >
          <Form.Item
            name="name"
            label="Название дисциплины"
            rules={[{ required: true, message: 'Введите название дисциплины' }]}
          >
            <Input placeholder="Например: Математический анализ" />
          </Form.Item>

          <Form.Item
            name="department"
            label="Подразделение"
            rules={[{ required: true, message: 'Выберите подразделение' }]}
          >
            <Select
              placeholder="Выберите подразделение"
              options={[
                { value: 'dept1', label: 'Кафедра 1' },
                { value: 'dept2', label: 'Кафедра 2' },
              ]}
            />
          </Form.Item>

          <Form.Item
            name="semester"
            label="Семестр"
            rules={[{ required: true, message: 'Выберите семестр' }]}
          >
            <Select
              placeholder="Выберите семестр"
              options={[
                { value: '1', label: '1 семестр' },
                { value: '2', label: '2 семестр' },
              ]}
            />
          </Form.Item>
        </Form>
      </Card>

      <Card title="Назначение преподавателей" style={{ marginTop: 16 }}>
        <Table
          rowSelection={{
            type: 'checkbox',
            selectedRowKeys: selectedTeachers,
            onChange: (selectedRowKeys) => {
              setSelectedTeachers(selectedRowKeys as string[]);
            },
          }}
          columns={teacherColumns}
          dataSource={teachers}
          rowKey="id"
        />
      </Card>

      <Card title="Назначение групп" style={{ marginTop: 16 }}>
        <Table
          rowSelection={{
            type: 'checkbox',
            selectedRowKeys: selectedGroups,
            onChange: (selectedRowKeys) => {
              setSelectedGroups(selectedRowKeys as string[]);
            },
          }}
          columns={groupColumns}
          dataSource={groups}
          rowKey="id"
        />

        <Button
          type="primary"
          onClick={() => form.submit()}
          style={{ marginTop: 16 }}
          loading={loading}
        >
          Создать дисциплину
        </Button>
      </Card>
    </div>
  );
};

export default CreateDiscipline;
