import { Line } from 'react-chartjs-2';
import { useState, useEffect } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import httpClient from '../../../api/httpClient';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const AverageGradeChart = () => {
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [
      {
        label: 'Средний балл',
        data: [],
        borderColor: '#1890ff',
        backgroundColor: 'rgba(24, 144, 255, 0.1)',
        tension: 0.3,
        fill: true,
      },
    ],
  });

  useEffect(() => {
    const fetchAverageGrades = async () => {
      try {
        // Сначала получаем информацию о текущем пользователе
        const userResponse = await httpClient.get('/auth/jwt/me');
        const studentId = userResponse.data.id;

        // Получаем данные за последние 6 месяцев
        const endDate = new Date();
        endDate.setDate(endDate.getDate() + 1); // Добавляем один день к конечной дате
        const startDate = new Date();
        startDate.setMonth(startDate.getMonth() - 6);

        const { data } = await httpClient.get(`/students/${studentId}/marks/avg-by-date`, {
          params: {
            date_from: startDate.toISOString().split('T')[0],
            date_to: endDate.toISOString().split('T')[0]
          }
        });

        // Форматируем даты для отображения
        const formattedData = data.items.map(item => ({
          date: new Date(item.date).toLocaleDateString('ru-RU', { month: 'long' }),
          value: item.value
        }));

        setChartData(prev => ({
          labels: formattedData.map(item => item.date),
          datasets: [{
            ...prev.datasets[0],
            data: formattedData.map(item => item.value)
          }]
        }));
      } catch (error) {
        console.error('Error fetching average grades:', error);
      }
    };

    fetchAverageGrades();
  }, []);

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom' as const,
        labels: {
          usePointStyle: true,
          padding: 20,
        },
      },
    },
    scales: {
      y: {
        min: 2,
        max: 5,
        grid: {
          color: 'rgba(0, 0, 0, 0.05)',
        },
      },
      x: {
        grid: {
          display: false,
        },
      },
    },
  };

  return (
    <div style={{ height: '300px', padding: '10px' }}>
      <Line data={chartData} options={options} />
    </div>
  );
};

export default AverageGradeChart;
