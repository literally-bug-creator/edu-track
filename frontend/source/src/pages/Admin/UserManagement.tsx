import { Card, Table, Select, message } from 'antd';
import { useState, useEffect } from 'react';
import type { TableColumnsType } from 'antd';
import type { TablePaginationConfig } from 'antd/es/table';
import type { SorterResult } from 'antd/es/table/interface';
import httpClient from '../../api/httpClient';

interface User {
  id: string;
  first_name: string;
  last_name: string;
  middle_name: string;
  username: string; // email в API
  role: number; // Добавляем поле role
  currentRole?: string | null;
}

interface UsersParams {
  page: number;
  perPage: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
}

const UserManagement = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(false);
  const [total, setTotal] = useState(0);
  const [params, setParams] = useState<UsersParams>({
    page: 1,
    perPage: 10,
    sortOrder: 'asc'
  });

  const fetchUsers = async (parameters: UsersParams) => {
    setLoading(true);
    try {
      const { data } = await httpClient.get('/users', {
        params: {
          page: parameters.page,
          perPage: parameters.perPage,
          sortBy: parameters.sortBy,
          sortOrder: parameters.sortOrder,
        }
      });
      setUsers(data.items);
      setTotal(data.total);
    } catch (error) {
      message.error('Ошибка при загрузке списка пользователей');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers(params);
  }, [params]);

  const handleTableChange = (
    pagination: TablePaginationConfig,
    _: any,
    sorter: SorterResult<User> | SorterResult<User>[]
  ) => {
    const currentSorter = Array.isArray(sorter) ? sorter[0] : sorter;
    setParams({
      ...params,
      page: pagination.current || 1,
      perPage: pagination.pageSize || 10,
      sortBy: currentSorter.field as string,
      sortOrder: currentSorter.order === 'descend' ? 'desc' : 'asc'
    });
  };

  const handleRoleChange = async (userId: string, newRole: string) => {
    try {
      await httpClient.patch(`/users/${userId}`, null, {
        params: {
          role: newRole // newRole уже содержит числовое значение
        }
      });
      message.success('Роль пользователя успешно изменена');
      fetchUsers(params);
    } catch (error) {
      message.error('Ошибка при изменении роли пользователя');
    }
  };

  const columns: TableColumnsType<User> = [
    { 
      title: 'ФИО', 
      key: 'name',
      sorter: true,
      render: (_, record) => 
        `${record.last_name} ${record.first_name} ${record.middle_name || ''}`.trim()
    },
    { 
      title: 'Email', 
      dataIndex: 'username', 
      key: 'email',
      sorter: true 
    },
    {
      title: 'Роль',
      key: 'role',
      render: (_, record) => (
        <Select
          style={{ width: 200 }}
          value={String(record.role)} // Используем значение из role
          onChange={(value) => handleRoleChange(record.id, value)}
          placeholder="Выберите роль"
          options={[
            { value: '0', label: 'Администратор' },
            { value: '1', label: 'Преподаватель' },
            { value: '2', label: 'Студент' },
          ]}
        />
      ),
    }
  ];

  return (
    <Card title="Управление пользователями" style={{ margin: 20 }}>
      <Table 
        columns={columns} 
        dataSource={users}
        rowKey="id"
        loading={loading}
        pagination={{
          current: params.page,
          pageSize: params.perPage,
          total: total,
          showSizeChanger: true,
          showQuickJumper: true,
          showTotal: (total) => `Всего ${total} записей`
        }}
        onChange={handleTableChange}
      />
    </Card>
  );
};

export default UserManagement;
