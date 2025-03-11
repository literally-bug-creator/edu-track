import { Card, Form, Input, Select, Button, Table, message } from 'antd';
import { useState } from 'react';
import type { TableColumnsType } from 'antd';

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
  const [form] = Form.useForm();

  const teacherColumns: TableColumnsType<Teacher> = [
    { title: 'ФИО', dataIndex: 'name', key: 'name' },
    { title: 'Кафедра', dataIndex: 'department', key: 'department' },
  ];

  const groupColumns: TableColumnsType<Group> = [
    { title: 'Название группы', dataIndex: 'name', key: 'name' },
    { title: 'Курс', dataIndex: 'course', key: 'course' },
  ];

  const mockTeachers: Teacher[] = [
    { id: '1', name: 'Иванов И.И.', department: 'Кафедра 1' },
    { id: '2', name: 'Петров П.П.', department: 'Кафедра 2' },
  ];

  const mockGroups: Group[] = [
    { id: '1', name: 'Группа 101', course: '1' },
    { id: '2', name: 'Группа 102', course: '1' },
  ];

  const handleSubmit = async (values: any) => {
    try {
      const disciplineData = {
        ...values,
        teachers: selectedTeachers,
        groups: selectedGroups,
      };
      console.log('Создание дисциплины:', disciplineData);
      message.success('Дисциплина успешно создана');
      form.resetFields();
      setSelectedTeachers([]);
      setSelectedGroups([]);
    } catch (error) {
      message.error('Ошибка при создании дисциплины');
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
          dataSource={mockTeachers}
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
          dataSource={mockGroups}
          rowKey="id"
        />

        <Button
          type="primary"
          onClick={() => form.submit()}
          style={{ marginTop: 16 }}
        >
          Создать дисциплину
        </Button>
      </Card>
    </div>
  );
};

export default CreateDiscipline;
