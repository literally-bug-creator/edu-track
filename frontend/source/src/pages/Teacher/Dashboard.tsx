import { Card, Col, Row, Select } from 'antd';
import { useState } from 'react';
import GroupsAverageChart from './components/GroupsAverageChart';
import WorkGradesDistribution from './components/WorkGradesDistribution';

const TeacherDashboard = () => {
  const [selectedWork, setSelectedWork] = useState<string>();

  const works = [
    { value: 'hw1', label: 'Домашняя работа №1 (Математика)' },
    { value: 'test1', label: 'Контрольная работа №1 (Математика)' },
    { value: 'hw2', label: 'Домашняя работа №2 (Физика)' },
  ];

  return (
    <div style={{ margin: 20 }}>
      <Row gutter={[16, 16]}>
        <Col span={24}>
          <Card title="Средний балл по группам">
            <GroupsAverageChart />
          </Card>
        </Col>
        <Col span={24}>
          <Card title="Распределение оценок по работе">
            <Select
              style={{ width: '100%', marginBottom: 16 }}
              placeholder="Выберите работу"
              options={works}
              value={selectedWork}
              onChange={setSelectedWork}
            />
            <WorkGradesDistribution workId={selectedWork} />
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default TeacherDashboard;
