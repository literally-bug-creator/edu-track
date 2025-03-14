import { LockOutlined, UserOutlined, MailOutlined } from '@ant-design/icons';
import { Button, Form, Input, Typography, Alert } from 'antd';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { register } from '../../api/auth';

const { Title } = Typography;

interface RegisterValues {
  username: string; // email
  password: string;
  first_name: string;
  middle_name: string;
  last_name: string;
}

const RegisterPage = () => {
  const [error, setError] = useState<string>('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (values: RegisterValues) => {
    try {
      setLoading(true);
      setError('');
      
      const { ...registerData } = values;
      await register(registerData);
      navigate('/student');
    } catch (err) {
      setError('Ошибка при регистрации');
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
          Регистрация
        </Title>
      
        {error && <Alert 
          message={error} 
          type="error" 
          showIcon 
          style={{ marginBottom: 24 }} 
        />}

        <Form<RegisterValues>
          name="register"
          onFinish={handleSubmit}
          layout="vertical"
          size="large"
        >
          <Form.Item
            label="Фамилия"
            name="last_name"
            rules={[{ required: true, message: 'Пожалуйста, введите фамилию!' }]}
          >
            <Input
              prefix={<UserOutlined />}
              placeholder="Иванов"
            />
          </Form.Item>

          <Form.Item
            label="Имя"
            name="first_name"
            rules={[{ required: true, message: 'Пожалуйста, введите имя!' }]}
          >
            <Input
              prefix={<UserOutlined />}
              placeholder="Иван"
            />
          </Form.Item>

          <Form.Item
            label="Отчество"
            name="middle_name"
            rules={[{ required: true, message: 'Пожалуйста, введите отчество!' }]}
          >
            <Input
              prefix={<UserOutlined />}
              placeholder="Иванович"
            />
          </Form.Item>

          <Form.Item
            label="Email"
            name="username"
            rules={[
              { required: true, message: 'Пожалуйста, введите email!' },
              { type: 'email', message: 'Некорректный email' }
            ]}
          >
            <Input
              prefix={<MailOutlined />}
              placeholder="example@university.ru"
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
            />
          </Form.Item>

          <Form.Item
            label="Подтверждение пароля"
            name="confirmPassword"
            dependencies={['password']}
            rules={[
              { required: true, message: 'Пожалуйста, подтвердите пароль!' },
              ({ getFieldValue }) => ({
                validator(_, value) {
                  if (!value || getFieldValue('password') === value) {
                    return Promise.resolve();
                  }
                  return Promise.reject(new Error('Пароли не совпадают!'));
                },
              }),
            ]}
          >
            <Input.Password
              prefix={<LockOutlined />}
              placeholder="••••••••"
            />
          </Form.Item>

          <Form.Item>
            <Button
              type="primary"
              htmlType="submit"
              block
              loading={loading}
            >
              Зарегистрироваться
            </Button>
          </Form.Item>
        </Form>

        <div style={{ textAlign: 'center', marginTop: 24 }}>
          <Button type="link" onClick={() => navigate('/login')}>
            Уже есть аккаунт? Войти
          </Button>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;
