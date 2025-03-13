import { useState, useEffect } from 'react';
import { Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
} from 'chart.js';
import httpClient from '../../../api/httpClient';

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale);

interface MarksQueryParams {
  student_id: number;
  page?: number;
  perPage?: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
  discipline_id?: number;
}

const GradesDistribution = () => {
  const [chartData, setChartData] = useState({
    labels: ['Отлично (5)', 'Хорошо (4)', 'Удовлетворительно (3)', 'Неудовлетворительно (2)'],
    datasets: [{
      data: [0, 0, 0, 0],
      backgroundColor: ['#52c41a', '#1890ff', '#faad14', '#ff4d4f'],
    }],
  });

  useEffect(() => {
    const fetchMarksDistribution = async () => {
      try {
        // Сначала получаем ID текущего пользователя
        const userResponse = await httpClient.get('/auth/jwt/me');
        const studentId = userResponse.data.id;
        
        // Затем получаем распределение оценок
        const { data } = await httpClient.get(`/students/${studentId}/marks/distribution`);
        
        const gradesData = data.item.items;
        
        setChartData(prev => ({
          ...prev,
          datasets: [{
            ...prev.datasets[0],
            data: [
              gradesData['5'] || 0,
              gradesData['4'] || 0,
              gradesData['3'] || 0,
              gradesData['2'] || 0
            ]
          }]
        }));
      } catch (error) {
        console.error('Error fetching marks distribution:', error);
      }
    };

    fetchMarksDistribution();
  }, []);

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
