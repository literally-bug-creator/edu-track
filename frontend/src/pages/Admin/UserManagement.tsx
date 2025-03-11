import { Card, Table, Select, message } from 'antd';
import type { TableColumnsType } from 'antd';

interface User {
  id: string;
  name: string;
  email: string;
  currentRole: string | null;
}

const UserManagement = () => {
  const handleRoleChange = (userId: string, newRole: string) => {
    // TODO: Здесь должен быть API-запрос на изменение роли
    console.log(`Changing role for user ${userId} to ${newRole}`);
    message.success('Роль пользователя успешно изменена');
  };

  const columns: TableColumnsType<User> = [
    { title: 'ФИО', dataIndex: 'name', key: 'name' },
    { title: 'Email', dataIndex: 'email', key: 'email' },
    {
      title: 'Роль',
      key: 'role',
      render: (_, record) => (
        <Select
          style={{ width: 200 }}
          value={record.currentRole || undefined}
          onChange={(value) => handleRoleChange(record.id, value)}
          placeholder="Выберите роль"
          options={[
            { value: 'student', label: 'Студент' },
            { value: 'teacher', label: 'Преподаватель' },
            { value: 'admin', label: 'Администратор' },
          ]}
        />
      ),
    }
  ];

  // Моковые данные для примера
  const mockUsers: User[] = [
    {
      id: '1',
      name: 'Иванов Иван Иванович',
      email: 'ivanov@edu.ru',
      currentRole: 'student'
    },
    {
      id: '2',
      name: 'Петров Петр Петрович',
      email: 'petrov@edu.ru',
      currentRole: 'teacher'
    },
    {
      id: '3',
      name: 'Сидоров Сидор Сидорович',
      email: 'sidorov@edu.ru',
      currentRole: null
    },
  ];

  return (
    <Card title="Управление пользователями" style={{ margin: 20 }}>
      <Table 
        columns={columns} 
        dataSource={mockUsers}
        rowKey="id"
      />
    </Card>
  );
};

export default UserManagement;
