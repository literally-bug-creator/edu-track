import { Card, Table, Button, Tag, message } from 'antd';
import type { TableColumnsType } from 'antd';

interface TeacherRequest {
  id: string;
  name: string;
  email: string;
  department: string;
  status: 'pending' | 'approved' | 'rejected';
  date: string;
}

const TeacherRequests = () => {
  const handleApprove = (id: string) => {
    message.success('Заявка одобрена');
  };

  const handleReject = (id: string) => {
    message.success('Заявка отклонена');
  };

  const columns: TableColumnsType<TeacherRequest> = [
    { title: 'ФИО', dataIndex: 'name', key: 'name' },
    { title: 'Email', dataIndex: 'email', key: 'email' },
    { title: 'Кафедра', dataIndex: 'department', key: 'department' },
    { title: 'Дата заявки', dataIndex: 'date', key: 'date' },
    {
      title: 'Статус',
      dataIndex: 'status',
      key: 'status',
      render: (status) => (
        <Tag color={
          status === 'approved' ? 'success' :
          status === 'rejected' ? 'error' :
          'processing'
        }>
          {status === 'approved' ? 'Одобрено' :
           status === 'rejected' ? 'Отклонено' :
           'На рассмотрении'}
        </Tag>
      ),
    },
    {
      title: 'Действия',
      key: 'actions',
      render: (_, record) => (
        <div style={{ display: 'flex', gap: 8 }}>
          <Button
            type="primary"
            onClick={() => handleApprove(record.id)}
            disabled={record.status !== 'pending'}
          >
            Одобрить
          </Button>
          <Button
            danger
            onClick={() => handleReject(record.id)}
            disabled={record.status !== 'pending'}
          >
            Отклонить
          </Button>
        </div>
      ),
    },
  ];

  const mockData: TeacherRequest[] = [
    {
      id: '1',
      name: 'Иванов Иван Иванович',
      email: 'ivanov@edu.ru',
      department: 'Кафедра информатики',
      status: 'pending',
      date: '2024-01-15',
    },
    // Добавьте больше тестовых данных при необходимости
  ];

  return (
    <Card title="Заявки на регистрацию преподавателей" style={{ margin: 20 }}>
      <Table columns={columns} dataSource={mockData} />
    </Card>
  );
};

export default TeacherRequests;
