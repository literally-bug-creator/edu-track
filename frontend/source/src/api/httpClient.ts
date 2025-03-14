import axios from 'axios';
import { logout } from './auth';

const httpClient = axios.create({
  baseURL: 'http://api:8000'
});

httpClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    // Проверяем, содержит ли токен префикс Bearer
    const bearerToken = token.startsWith('Bearer ') ? token : `Bearer ${token}`;
    // Убедимся, что headers существует
    config.headers = config.headers || {};
    config.headers.Authorization = bearerToken;
  }
  return config;
});

httpClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      logout();
    }
    return Promise.reject(error);
  }
);

export default httpClient;
