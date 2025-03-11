import { useState } from 'react';
import { Select, Table, Card } from 'antd';
import type { TableColumnsType } from 'antd';

interface Mark {
  id: number;
  discipline: string;
  workType: string;
  score: number;
  date: string;
}

const Marks = () => {
  const [selectedDiscipline, setSelectedDiscipline] = useState<string>();
  const [selectedWorkType, setSelectedWorkType] = useState<string>();

  // Примерные данные (замените на реальные данные с API)
  const disciplines = [
    { value: 'math', label: 'Математика' },
    { value: 'physics', label: 'Физика' },
    { value: 'programming', label: 'Программирование' },
  ];

  const workTypes = [
    { value: 'homework', label: 'Домашняя работа' },
    { value: 'test', label: 'Тест' },
    { value: 'exam', label: 'Экзамен' },
  ];

  const columns: TableColumnsType<Mark> = [
    {
      title: 'Дисциплина',
      dataIndex: 'discipline',
      key: 'discipline',
    },
    {
      title: 'Тип работы',
      dataIndex: 'workType',
      key: 'workType',
    },
    {
      title: 'Оценка',
      dataIndex: 'score',
      key: 'score',
    },
    {
      title: 'Дата',
      dataIndex: 'date',
      key: 'date',
    },
  ];

  const marks: Mark[] = [
    {
      id: 1,
      discipline: 'Математика',
      workType: 'Домашняя работа',
      score: 5,
      date: '2024-01-15',
    },
    // Добавьте больше данных здесь
  ];

  return (
    <Card title="Мои оценки" style={{ margin: 20 }}>
      <div style={{ display: 'flex', gap: 16, marginBottom: 20 }}>
        <Select
          style={{ width: 200 }}
          placeholder="Выберите дисциплину"
          options={disciplines}
          value={selectedDiscipline}
          onChange={setSelectedDiscipline}
        />
        <Select
          style={{ width: 200 }}
          placeholder="Выберите тип работы"
          options={workTypes}
          value={selectedWorkType}
          onChange={setSelectedWorkType}
        />
      </div>
      <Table
        columns={columns}
        dataSource={marks}
        rowKey="id"
      />
    </Card>
  );
};

export default Marks;
