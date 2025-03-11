import { Table } from 'antd';
import { useState, useEffect } from 'react';

const SubjectsList = () => {
  const [subjects, setSubjects] = useState([]);

  const columns = [
    {
      title: 'Предмет',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Средний балл',
      dataIndex: 'averageGrade',
      key: 'averageGrade',
    },
  ];

  // TODO: Добавить загрузку данных с API
  useEffect(() => {
    // Временные данные для примера
    setSubjects([
      { key: '1', name: 'Математика', averageGrade: 4.5 },
      { key: '2', name: 'Физика', averageGrade: 4.0 },
    ]);
  }, []);

  return <Table columns={columns} dataSource={subjects} />;
};

export default SubjectsList;
