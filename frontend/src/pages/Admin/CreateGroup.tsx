import { Card, Form, Input, Select, Button, Table, message } from 'antd';
import { useState } from 'react';
import type { TableColumnsType } from 'antd';

interface Student {
  id: string;
  name: string;
  email: string;
}

const CreateGroup = () => {
  const [selectedStudents, setSelectedStudents] = useState<string[]>([]);
  const [form] = Form.useForm();

  const columns: TableColumnsType<Student> = [
    { title: 'ФИО', dataIndex: 'name', key: 'name' },
    { title: 'Email', dataIndex: 'email', key: 'email' },
  ];

  const mockStudents: Student[] = [
    { id: '1', name: 'Иванов И.И.', email: 'ivanov@edu.ru' },
    { id: '2', name: 'Петров П.П.', email: 'petrov@edu.ru' },
  ];

  const handleSubmit = async (values: any) => {
    try {
      const groupData = {
        ...values,
        students: selectedStudents,
      };
      console.log('Создание группы:', groupData);
      message.success('Группа успешно создана');
      form.resetFields();
      setSelectedStudents([]);
    } catch (error) {
      message.error('Ошибка при создании группы');
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <Card title="Создание новой группы">
        <Form
          form={form}
          layout="vertical"
          onFinish={handleSubmit}
        >
          <Form.Item
            name="name"
            label="Название группы"
            rules={[{ required: true, message: 'Введите название группы' }]}
          >
            <Input placeholder="Например: Группа 101" />
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
            name="course"
            label="Курс"
            rules={[{ required: true, message: 'Выберите курс' }]}
          >
            <Select
              placeholder="Выберите курс"
              options={[
                { value: '1', label: '1 курс' },
                { value: '2', label: '2 курс' },
              ]}
            />
          </Form.Item>
        </Form>
      </Card>

      <Card title="Добавление студентов" style={{ marginTop: 16 }}>
        <Table
          rowSelection={{
            type: 'checkbox',
            selectedRowKeys: selectedStudents,
            onChange: (selectedRowKeys) => {
              setSelectedStudents(selectedRowKeys as string[]);
            },
          }}
          columns={columns}
          dataSource={mockStudents}
          rowKey="id"
        />

        <Button
          type="primary"
          onClick={() => form.submit()}
          style={{ marginTop: 16 }}
        >
          Создать группу
        </Button>
      </Card>
    </div>
  );
};

export default CreateGroup;
