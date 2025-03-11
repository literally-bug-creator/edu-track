import { Layout, Menu, Button } from 'antd';
import { useNavigate, useLocation, Outlet } from 'react-router-dom';
import { 
  DashboardOutlined, 
  UserOutlined, 
  TeamOutlined, 
  BookOutlined,
  LogoutOutlined 
} from '@ant-design/icons';

const { Content, Header } = Layout;

const AdminLayout = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const menuItems = [
    {
      key: '/admin/dashboard',
      icon: <DashboardOutlined />,
      label: 'Дашборд',
    },
    {
      key: '/admin/users',
      icon: <UserOutlined />,
      label: 'Пользователи',
    },
    {
      key: '/admin/groups',
      icon: <TeamOutlined />,
      label: 'Создать группу',
    },
    {
      key: '/admin/disciplines',
      icon: <BookOutlined />,
      label: 'Создать дисциплину',
    },
  ];

  const handleLogout = () => {
    navigate('/login');
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ 
        background: '#fff', 
        padding: '0 24px',
        display: 'flex',
        alignItems: 'center',
        boxShadow: '0 2px 8px rgba(0, 0, 0, 0.15)',
      }}>
        <div style={{
          fontSize: '20px',
          fontWeight: 'bold',
          width: '200px',
        }}>
          EduTrack
        </div>
        <Menu
          mode="horizontal"
          selectedKeys={[location.pathname]}
          items={menuItems}
          onClick={({ key }) => navigate(key)}
          style={{ 
            flex: 1,
            display: 'flex',
            justifyContent: 'center',
            fontSize: '16px',
          }}
        />
        <div style={{ width: '200px', display: 'flex', justifyContent: 'flex-end' }}>
          <Button 
            icon={<LogoutOutlined />}
            onClick={handleLogout}
            type="text"
            size="large"
          >
            Выйти
          </Button>
        </div>
      </Header>
      <Content style={{ 
        margin: '24px',
        minHeight: 280,
        background: '#fff',
        borderRadius: '8px'
      }}>
        <Outlet />
      </Content>
    </Layout>
  );
};

export default AdminLayout;
