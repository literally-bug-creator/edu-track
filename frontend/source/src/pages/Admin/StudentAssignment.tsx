import { useState, useEffect } from 'react';
import { Card, Table, Select, message } from 'antd';
import { getStudents, getGroups, updateStudent, Student } from '../../api/students';

interface GroupResponse {
  id: number;
  number: string;
}

const StudentAssignment = () => {
  const [students, setStudents] = useState<Student[]>([]);
  const [groups, setGroups] = useState<GroupResponse[]>([]);
  const [loading, setLoading] = useState(false);

  const fetchData = async () => {
    setLoading(true);
    try {
      const [studentsRes, groupsRes] = await Promise.all([
        getStudents(),
        getGroups()
      ]);
      
      if (studentsRes.data?.items && groupsRes.data?.items) {
        setStudents(studentsRes.data.items);
        setGroups(groupsRes.data.items);
      }
    } catch (error) {
      message.error('Ошибка при загрузке данных');
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleGroupChange = async (groupId: number | undefined, studentId: number) => {
    try {
      await updateStudent(studentId, { group_id: groupId });
      message.success('Группа успешно обновлена');
      fetchData();
    } catch (error) {
      message.error('Ошибка при обновлении группы');
    }
  };

  const columns = [
    {
      title: 'Фамилия',
      dataIndex: 'last_name',
      key: 'last_name',
    },
    {
      title: 'Имя',
      dataIndex: 'first_name',
      key: 'first_name',
    },
    {
      title: 'Отчество',
      dataIndex: 'middle_name',
      key: 'middle_name',
    },
    {
      title: 'Группа',
      dataIndex: 'group_id',
      key: 'group_id',
      render: (_: any, record: Student) => (
        <Select
          style={{ width: 200 }}
          value={record.group_id}
          onChange={(value) => handleGroupChange(value, record.id)}
          options={groups.map(group => ({ 
            value: group.id, 
            label: group.number
          }))}
          allowClear
          placeholder="Выберите группу"
        />
      ),
    },
  ];

  return (
    <Card title="Назначение студентов в группы" style={{ margin: 20 }}>
      <Table
        columns={columns}
        dataSource={students}
        rowKey="id"
        loading={loading}
      />
    </Card>
  );
};

export default StudentAssignment;
