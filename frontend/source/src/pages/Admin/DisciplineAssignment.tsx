import React, { useEffect, useState } from 'react';
import { Card, Table, Select, Button, message, Row, Col } from 'antd';
import axios from 'axios';
import httpClient from '../../api/httpClient';

interface Teacher {
  id: number;
  first_name: string;
  last_name: string;
  middle_name: string;
}

interface Group {
  id: number;
  number: string;
}

interface Discipline {
  id: number;
  name: string;
}

interface PaginatedResponse<T> {
  items: T[];
  total: number;
}

const DisciplineAssignment: React.FC = () => {
  const [disciplines, setDisciplines] = useState<Discipline[]>([]);
  const [teachers, setTeachers] = useState<Teacher[]>([]);
  const [groups, setGroups] = useState<Group[]>([]);
  const [selectedDiscipline, setSelectedDiscipline] = useState<number | null>(null);
  const [selectedTeacher, setSelectedTeacher] = useState<number | null>(null);
  const [selectedGroup, setSelectedGroup] = useState<number | null>(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [disciplinesRes, teachersRes, groupsRes] = await Promise.all([
        httpClient.get<PaginatedResponse<Discipline>>('/disciplines'),
        httpClient.get<PaginatedResponse<Teacher>>('/teachers'),
        httpClient.get<PaginatedResponse<Group>>('/groups')
      ]);

    //   console.log('Loaded data:', { 
    //     disciplines: disciplinesRes.data.items,
    //     teachers: teachersRes.data.items,
    //     groups: groupsRes.data.items 
    //   });

      setDisciplines(disciplinesRes.data.items);
      setTeachers(teachersRes.data.items);
      setGroups(groupsRes.data.items);
    } catch (error) {
      message.error('Ошибка при загрузке данных');
    }
  };

  const handleTeacherAssignment = async () => {
    if (!selectedDiscipline || !selectedTeacher) {
      message.warning('Выберите дисциплину и преподавателя');
      return;
    }

    try {
      const response = await httpClient.put(`/disciplines/${selectedDiscipline}/teachers/${selectedTeacher}`);
    //   console.log('Teacher assignment response:', response);
      message.success('Преподаватель успешно назначен на дисциплину');
      setSelectedDiscipline(null);
      setSelectedTeacher(null);
      fetchData();
    } catch (error: any) {
    //   console.error('Teacher assignment error:', error.response?.data || error);
      message.error('Ошибка при назначении преподавателя: ' + (error.response?.data?.message || 'Неизвестная ошибка'));
    }
  };

  const handleGroupAssignment = async () => {
    if (!selectedDiscipline || !selectedGroup) {
      message.warning('Выберите дисциплину и группу');
      return;
    }

    try {
      const response = await httpClient.put(`/disciplines/${selectedDiscipline}/groups/${selectedGroup}`);
    //   console.log('Group assignment response:', response);
      message.success('Группа успешно назначена на дисциплину');
      setSelectedDiscipline(null);
      setSelectedGroup(null);
      fetchData();
    } catch (error: any) {
    //   console.error('Group assignment error:', error.response?.data || error);
      message.error('Ошибка при назначении группы: ' + (error.response?.data?.message || 'Неизвестная ошибка'));
    }
  };

  return (
    <div>
      <Card title="Назначение преподавателя на дисциплину" style={{ marginBottom: 16 }}>
        <Row gutter={[16, 16]}>
          <Col span={12}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите дисциплину"
              value={selectedDiscipline}
              onChange={(value) => setSelectedDiscipline(value)}
            >
              {disciplines.map(discipline => (
                <Select.Option key={discipline.id} value={discipline.id}>
                  {discipline.name}
                </Select.Option>
              ))}
            </Select>
          </Col>
          <Col span={12}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите преподавателя"
              value={selectedTeacher}
              onChange={(value) => setSelectedTeacher(value)}
            >
              {teachers.map(teacher => (
                <Select.Option key={teacher.id} value={teacher.id}>
                  {`${teacher.last_name} ${teacher.first_name} ${teacher.middle_name}`}
                </Select.Option>
              ))}
            </Select>
          </Col>
        </Row>
        <Row style={{ marginTop: 16 }}>
          <Col>
            <Button type="primary" onClick={handleTeacherAssignment}>
              Назначить преподавателя
            </Button>
          </Col>
        </Row>
      </Card>

      <Card title="Назначение группы на дисциплину">
        <Row gutter={[16, 16]}>
          <Col span={12}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите дисциплину"
              value={selectedDiscipline}
              onChange={(value) => setSelectedDiscipline(value)}
            >
              {disciplines.map(discipline => (
                <Select.Option key={discipline.id} value={discipline.id}>
                  {discipline.name}
                </Select.Option>
              ))}
            </Select>
          </Col>
          <Col span={12}>
            <Select
              style={{ width: '100%' }}
              placeholder="Выберите группу"
              value={selectedGroup}
              onChange={(value) => setSelectedGroup(value)}
            >
              {groups.map(group => (
                <Select.Option key={group.id} value={group.id}>
                  {group.number}
                </Select.Option>
              ))}
            </Select>
          </Col>
        </Row>
        <Row style={{ marginTop: 16 }}>
          <Col>
            <Button type="primary" onClick={handleGroupAssignment}>
              Назначить группу
            </Button>
          </Col>
        </Row>
      </Card>
    </div>
  );
};

export default DisciplineAssignment;
