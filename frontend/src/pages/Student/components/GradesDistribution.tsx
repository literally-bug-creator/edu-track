import { useState, useEffect } from 'react';
import { Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
} from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale);

const GradesDistribution = () => {
  const [chartData, setChartData] = useState({
    labels: ['Отлично (5)', 'Хорошо (4)', 'Удовлетворительно (3)', 'Неудовлетворительно (2)'],
    datasets: [{
      data: [4, 6, 2, 1],
      backgroundColor: ['#52c41a', '#1890ff', '#faad14', '#ff4d4f'],
    }],
  });

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom' as const,
        labels: {
          padding: 20,
          usePointStyle: true,
        },
      },
    },
  };

  return (
    <div style={{ height: '300px', padding: '10px' }}>
      <Pie data={chartData} options={options} />
    </div>
  );
};

export default GradesDistribution;
