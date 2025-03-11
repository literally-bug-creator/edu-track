import { Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
} from 'chart.js';
import { Empty } from 'antd';

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale);

interface Props {
  workId?: string;
}

const WorkGradesDistribution = ({ workId }: Props) => {
  if (!workId) {
    return <Empty description="Выберите работу для просмотра статистики" />;
  }

  const data = {
    labels: ['Отлично (5)', 'Хорошо (4)', 'Удовлетворительно (3)', 'Неудовлетворительно (2)'],
    datasets: [{
      data: [8, 12, 4, 2],
      backgroundColor: ['#52c41a', '#1890ff', '#faad14', '#ff4d4f'],
    }],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom' as const,
      },
    },
  };

  return (
    <div style={{ height: '400px' }}>
      <Pie data={data} options={options} />
    </div>
  );
};

export default WorkGradesDistribution;
