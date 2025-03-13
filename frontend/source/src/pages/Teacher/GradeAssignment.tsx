import { Card, Form, Select, InputNumber, Button, Table, message } from 'antd';
import { useState } from 'react';
import type { TableColumnsType } from 'antd';

interface Student {
  id: number;
  fullName: string;
  grade?: number;
}

const GradeAssignment = () => {
  const [selectedStudents, setSelectedStudents] = useState<Student[]>([]);
  const [form] = Form.useForm();

  // Моковые данные (замените на реальные API-вызовы)
  const disciplines = [
    { value: 'math', label: 'Математика' },
    { value: 'physics', label: 'Физика' },
    { value: 'programming', label: 'Программирование' },
  ];

  const groups = [
    { value: 'group1', label: 'Группа 101' },
    { value: 'group2', label: 'Группа 102' },
    { value: 'group3', label: 'Группа 103' },
  ];

  const workTypes = [
    { value: 'homework', label: 'Домашняя работа' },
    { value: 'test', label: 'Тест' },
    { value: 'exam', label: 'Экзамен' },
  ];

  // Имитация загрузки студентов при выборе группы
  const handleGroupChange = (groupId: string) => {
    // Здесь должен быть API-вызов для получения студентов группы
    const mockStudents: Student[] = [
      { id: 1, fullName: 'Иванов Иван Иванович' },
      { id: 2, fullName: 'Петров Петр Петрович' },
      { id: 3, fullName: 'Сидорова Анна Павловна' },
    ];
    setSelectedStudents(mockStudents);
  };

  const columns: TableColumnsType<Student> = [
    {
      title: 'ФИО студента',
      dataIndex: 'fullName',
      key: 'fullName',
    },
    {
      title: 'Оценка',
      key: 'grade',
      render: (_, student) => (
        <InputNumber
          min={2}
          max={5}
          onChange={(value) => {
            const updated = selectedStudents.map(s => 
              s.id === student.id ? { ...s, grade: value } : s
            );
            setSelectedStudents(updated);
          }}
        />
      ),
    },
  ];

  const handleSubmit = async () => {
    const formValues = await form.validateFields();
    const gradesToSubmit = selectedStudents
      .filter(s => s.grade)
      .map(s => ({
        studentId: s.id,
        grade: s.grade,
        ...formValues
      }));
    
    // Здесь должен быть API-вызов для сохранения оценок
    console.log('Отправка оценок:', gradesToSubmit);
    message.success('Оценки успешно выставлены');
  };

  return (
    <Card title="Выставление оценок" style={{ margin: 20 }}>
      <Form
        form={form}
        layout="vertical"
      >
        <div style={{ display: 'flex', gap: 16, marginBottom: 20 }}>
          <Form.Item
            name="discipline"
            label="Дисциплина"
            rules={[{ required: true, message: 'Выберите дисциплину' }]}
            style={{ width: 200 }}
          >
            <Select
              options={disciplines}
              placeholder="Выберите дисциплину"
            />
          </Form.Item>

          <Form.Item
            name="group"
            label="Группа"
            rules={[{ required: true, message: 'Выберите группу' }]}
            style={{ width: 200 }}
          >
            <Select
              options={groups}
              placeholder="Выберите группу"
              onChange={handleGroupChange}
            />
          </Form.Item>

          <Form.Item
            name="workType"
            label="Тип работы"
            rules={[{ required: true, message: 'Выберите тип работы' }]}
            style={{ width: 200 }}
          >
            <Select
              options={workTypes}
              placeholder="Выберите тип работы"
            />
          </Form.Item>
        </div>

        <Table
          columns={columns}
          dataSource={selectedStudents}
          rowKey="id"
          pagination={false}
          style={{ marginBottom: 20 }}
        />

        <Button type="primary" onClick={handleSubmit}>
          Сохранить оценки
        </Button>
      </Form>
    </Card>
  );
};

export default GradeAssignment;
