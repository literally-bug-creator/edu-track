import { Card, Form, Select, InputNumber, Button, Table, message } from 'antd';
import { useState, useEffect } from 'react';
import type { TableColumnsType } from 'antd';
import httpClient from '../../api/httpClient';

interface Student {
  id: number;
  fullName: string;
  grade?: number | null;
}

interface Teacher {
  id: number;
  username: string;
  first_name: string;
  middle_name: string;
  last_name: string;
  role: number;
  group_id: number;
}

interface Discipline {
  id: number;
  name: string;
  track_id: number;
  course_number: number;
  semester_number: number;
}

interface Group {
  id: number;
  number: string;
  track_id: number;
}

interface DisciplinesResponse {
  items: Discipline[];
  total: number;
}

interface StudentResponse {
  id: number;
  username: string;
  first_name: string;
  middle_name: string;
  last_name: string;
  role: number;
  group_id: number;
}

interface StudentsListResponse {
  items: StudentResponse[];
  total: number;
}

interface MarkRequest {
  discipline_id: number;
  student_id: number;
  work_type: number;
  type: number;
}

const GradeAssignment = () => {
  const [selectedStudents, setSelectedStudents] = useState<Student[]>([]);
  const [disciplines, setDisciplines] = useState<{ value: number; label: string }[]>([]);
  const [groups, setGroups] = useState<{ value: number; label: string }[]>([]);
  const [teacherId, setTeacherId] = useState<number | null>(null);
  const [loading, setLoading] = useState(true);
  const [form] = Form.useForm();

  useEffect(() => {
    const fetchTeacherData = async () => {
      try {
        const response = await httpClient.get<Teacher>('/auth/jwt/me');
        setTeacherId(response.data.id);
      } catch (error) {
        message.error('Ошибка при получении данных преподавателя');
      }
    };
    fetchTeacherData();
  }, []);

  useEffect(() => {
    const fetchDisciplines = async () => {
      if (!teacherId) return;
      
      try {
        const response = await httpClient.get<DisciplinesResponse>(`/teachers/${teacherId}/disciplines`, {
          params: {
            page: 1,
            perPage: 100,
            sortBy: 'name',
            sortOrder: 'asc'
          }
        });
        
        setDisciplines(response.data.items.map(discipline => ({
          value: discipline.id,
          label: discipline.name
        })));
      } catch (error) {
        message.error('Ошибка при загрузке дисциплин');
      } finally {
        setLoading(false);
      }
    };

    if (teacherId) {
      fetchDisciplines();
    }
  }, [teacherId]);

  const handleDisciplineChange = async (disciplineId: number) => {
    try {
      const response = await httpClient.get<{items: Group[], total: number}>(`/disciplines/${disciplineId}/groups`);
      setGroups(response.data.items.map(group => ({
        value: group.id,
        label: group.number
      })));
    } catch (error) {
      message.error('Ошибка при загрузке групп');
    }
  };

  const workTypes = [
    { value: 0, label: 'Домашняя работа' },
    { value: 1, label: 'Практическая работа' },
    { value: 2, label: 'Лабораторная работа' },
    { value: 3, label: 'Контрольная работа' },
    { value: 4, label: 'Курсовая работа' },
  ];

  const handleGroupChange = async (groupId: string) => {
    if (!teacherId) return;
    
    try {
      const response = await httpClient.get<StudentsListResponse>(`/teachers/${teacherId}/groups/${groupId}/students`, {
        params: {
          page: 1,
          perPage: 100,
          sortBy: 'last_name',
          sortOrder: 'asc'
        }
      });
      
      setSelectedStudents(response.data.items.map(student => ({
        id: student.id,
        fullName: `${student.last_name} ${student.first_name} ${student.middle_name}`,
      })));
    } catch (error) {
      message.error('Ошибка при загрузке списка студентов');
      setSelectedStudents([]);
    }
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
          value={student.grade}
          onChange={(value: number | null) => {
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
    try {
      const formValues = await form.validateFields();
      const promises = selectedStudents
        .filter(s => s.grade)
        .map(student => {
          const markData: MarkRequest = {
            discipline_id: formValues.discipline,
            student_id: student.id,
            type: student.grade || 2,
            work_type: formValues.workType,
          };
          return httpClient.put('/marks', markData);
        });

      await Promise.all(promises);
      message.success('Оценки успешно выставлены');
      
      setSelectedStudents([]);
      form.resetFields();
    } catch (error) {
      message.error('Ошибка при сохранении оценок');
    }
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
              loading={loading}
              onChange={handleDisciplineChange}
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
