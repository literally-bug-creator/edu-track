const API_URL = 'http://api:8000';

interface LoginResponse {
  access_token: string;
  token_type: string;
}

export interface RegisterRequest {
  last_name: string;
  first_name: string;
  middle_name: string;
  username: string;
  password: string;
}

interface UserInfo {
  id: number;
  username: string;
  first_name: string;
  middle_name: string;
  last_name: string;
  role: number;
  group_id: number;
}

export const login = async (email: string, password: string): Promise<LoginResponse> => {
  const formData = new URLSearchParams();
  formData.append('username', email);
  formData.append('password', password);

  const response = await fetch(`${API_URL}/auth/jwt/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData.toString(),
  });

  if (!response.ok) {
    throw new Error('Ошибка авторизации');
  }

  const data = await response.json();
  
  if (!data.access_token) {
    throw new Error('Некорректный ответ от сервера');
  }

  // Сохраняем полный токен с префиксом Bearer
  localStorage.setItem('token', `${data.token_type} ${data.access_token}`);

  return data;
};

export const getCurrentUser = async (): Promise<UserInfo> => {
  const token = localStorage.getItem('token');
  if (!token) {
    throw new Error('Не авторизован');
  }

  const response = await fetch(`${API_URL}/auth/jwt/me`, {
    headers: {
      'Authorization': token // Теперь token уже содержит "Bearer "
    }
  });

  if (!response.ok) {
    if (response.status === 401) {
      logout();
    }
    throw new Error('Ошибка получения данных пользователя');
  }

  return response.json();
};

export const isAuthenticated = (): boolean => {
  const token = localStorage.getItem('token');
  return !!token;
};

export const validateToken = async (): Promise<boolean> => {
  try {
    await getCurrentUser();
    return true;
  } catch {
    return false;
  }
};

export const logout = (): void => {
  localStorage.removeItem('token');
  localStorage.removeItem('user');
  window.location.href = '/login';
};

export const register = async (data: RegisterRequest): Promise<void> => {
  const formData = new URLSearchParams();
  Object.entries(data).forEach(([key, value]) => {
    formData.append(key, value);
  });

  const response = await fetch(`${API_URL}/auth/jwt/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData.toString(),
  });

  if (!response.ok) {
    throw new Error('Ошибка при регистрации');
  }
};
