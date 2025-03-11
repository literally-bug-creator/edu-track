import { Card, Col, Row } from 'antd';
import SubjectsList from './components/SubjectsList';
import GradesDistribution from './components/GradesDistribution';
import AverageGradeChart from './components/AverageGradeChart';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <Row gutter={[16, 16]}>
        <Col span={24} lg={12}>
          <Card title="Предметы и средние баллы" bodyStyle={{ padding: '0 10px' }}>
            <SubjectsList />
          </Card>
        </Col>
        <Col span={24} lg={12}>
          <Card title="Распределение оценок" bodyStyle={{ padding: '10px' }}>
            <GradesDistribution />
          </Card>
        </Col>
        <Col span={24}>
          <Card title="Динамика среднего балла" bodyStyle={{ padding: '10px' }}>
            <AverageGradeChart />
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default Dashboard;
