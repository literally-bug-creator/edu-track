import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const GroupsAverageChart = () => {
  // Моковые данные - заменить на реальные с API
  const data = {
    labels: ['Группа 101', 'Группа 102', 'Группа 103', 'Группа 201'],
    datasets: [
      {
        label: 'Средний балл',
        data: [4.2, 3.8, 4.5, 4.1],
        backgroundColor: '#1890ff',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom' as const,
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 5,
      },
    },
  };

  return (
    <div style={{ height: '400px' }}>
      <Bar data={data} options={options} />
    </div>
  );
};

export default GroupsAverageChart;
