import { Card, Col, Row, Select, Table } from 'antd';
import { useState } from 'react';
import type { TableColumnsType } from 'antd';

interface Student {
  id: string;
  name: string;
  group: string;
  averageGrade: number;
}

const Dashboard = () => {
  const [selectedTeacher, setSelectedTeacher] = useState<string>();
  const [selectedDepartment, setSelectedDepartment] = useState<string>();
  const [selectedProgram, setSelectedProgram] = useState<string>();
  const [selectedCourse, setSelectedCourse] = useState<string>();
  const [selectedSemester, setSelectedSemester] = useState<string>();
  const [selectedDiscipline, setSelectedDiscipline] = useState<string>();
  const [selectedGroup, setSelectedGroup] = useState<string>();
  const [selectedStudent, setSelectedStudent] = useState<string>();

  const columns: TableColumnsType<Student> = [
    { title: 'ФИО', dataIndex: 'name', key: 'name' },
    { title: 'Группа', dataIndex: 'group', key: 'group' },
    { title: 'Средний балл', dataIndex: 'averageGrade', key: 'averageGrade' },
  ];

  const mockData: Student[] = [
    { id: '1', name: 'Иванов И.И.', group: 'Группа 101', averageGrade: 4.5 },
    { id: '2', name: 'Петров П.П.', group: 'Группа 101', averageGrade: 4.2 },
  ];

  return (
    <div style={{ padding: 20 }}>
      <Card title="Фильтры">
        <Row gutter={[16, 16]}>
          <Col span={8}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите преподавателя"
              value={selectedTeacher}
              onChange={setSelectedTeacher}
              options={[
                { value: 'teacher1', label: 'Преподаватель 1' },
                { value: 'teacher2', label: 'Преподаватель 2' },
              ]}
            />
          </Col>
          <Col span={8}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите подразделение"
              value={selectedDepartment}
              onChange={setSelectedDepartment}
              options={[
                { value: 'dept1', label: 'Кафедра 1' },
                { value: 'dept2', label: 'Кафедра 2' },
              ]}
            />
          </Col>
          <Col span={8}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите направление"
              value={selectedProgram}
              onChange={setSelectedProgram}
              options={[
                { value: 'prog1', label: 'Направление 1' },
                { value: 'prog2', label: 'Направление 2' },
              ]}
            />
          </Col>
          <Col span={8}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите курс"
              value={selectedCourse}
              onChange={setSelectedCourse}
              options={[
                { value: '1', label: '1 курс' },
                { value: '2', label: '2 курс' },
              ]}
            />
          </Col>
          <Col span={8}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите семестр"
              value={selectedSemester}
              onChange={setSelectedSemester}
              options={[
                { value: '1', label: '1 семестр' },
                { value: '2', label: '2 семестр' },
              ]}
            />
          </Col>
          <Col span={8}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите дисциплину"
              value={selectedDiscipline}
              onChange={setSelectedDiscipline}
              options={[
                { value: 'disc1', label: 'Дисциплина 1' },
                { value: 'disc2', label: 'Дисциплина 2' },
              ]}
            />
          </Col>
          <Col span={8}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите группу"
              value={selectedGroup}
              onChange={setSelectedGroup}
              options={[
                { value: 'group1', label: 'Группа 101' },
                { value: 'group2', label: 'Группа 102' },
              ]}
            />
          </Col>
          <Col span={8}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите студента"
              value={selectedStudent}
              onChange={setSelectedStudent}
              options={[
                { value: 'student1', label: 'Иванов И.И.' },
                { value: 'student2', label: 'Петров П.П.' },
              ]}
            />
          </Col>
        </Row>
      </Card>

      <Card title="Результаты" style={{ marginTop: 16 }}>
        <Table columns={columns} dataSource={mockData} />
      </Card>
    </div>
  );
};

export default Dashboard;
