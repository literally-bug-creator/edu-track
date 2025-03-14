import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Form, Input, Typography, Alert } from 'antd';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { login, getCurrentUser } from '../../api/auth';

const { Title } = Typography;

interface LoginValues {
  email: string;
  password: string;
  role?: 'student' | 'teacher' | 'admin';
}

const LoginPage = () => {
  const [error, setError] = useState<string>('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (values: LoginValues) => {
    try {
      setLoading(true);
      setError('');
      
      await login(values.email, values.password);
      
      // Получаем информацию о пользователе
      const userInfo = await getCurrentUser();
      
      // Сразу перенаправляем на нужную страницу
      if (userInfo.role === 0) {
        navigate('/admin/users', { replace: true });
      } else if (userInfo.role === 1) {
        navigate('/teacher/grade-assignment', { replace: true });
      } else {
        navigate('/student/dashboard', { replace: true });
      }
    } catch (err) {
      setError('Неверный email или пароль');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)',
      padding: '20px'
    }}>
      <div style={{
        width: '100%',
        maxWidth: 400,
        padding: 32,
        backgroundColor: 'white',
        borderRadius: 8,
        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
      }}>
        <Title level={2} style={{ 
          textAlign: 'center', 
          marginBottom: 32,
          color: '#1890ff',
          fontSize: '28px'
        }}>
          Вход в систему
        </Title>
      
        {error && <Alert 
          message={error} 
          type="error" 
          showIcon 
          style={{ marginBottom: 24 }} 
        />}

        <Form<LoginValues>
          name="login"
          initialValues={{ remember: true }}
          onFinish={handleSubmit}
          layout="vertical"
          size="large"
        >
          <Form.Item
            label="Email"
            name="email"
            rules={[
              { required: true, message: 'Пожалуйста, введите email!' },
              { type: 'email', message: 'Некорректный email' }
            ]}
          >
            <Input
              prefix={<UserOutlined />}
              placeholder="example@university.ru"
              size="large"
            />
          </Form.Item>

          <Form.Item
            label="Пароль"
            name="password"
            rules={[{ required: true, message: 'Пожалуйста, введите пароль!' }]}
          >
            <Input.Password
              prefix={<LockOutlined />}
              placeholder="••••••••"
              size="large"
            />
          </Form.Item>

          <Form.Item>
            <Button
              type="primary"
              htmlType="submit"
              block
              size="large"
              loading={loading}
            >
              Войти
            </Button>
          </Form.Item>
        </Form>

        <div style={{ textAlign: 'center', marginTop: 24 }}>
          {/* <Button type="link" style={{ fontSize: '16px' }}>
            Забыли пароль?
          </Button> */}
          <Button type="link" onClick={() => navigate('/register')} style={{ fontSize: '16px' }}>
            Зарегистрироваться
          </Button>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;