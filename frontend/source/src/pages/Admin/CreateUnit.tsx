import { Card, Form, Input, Button, message, Table } from 'antd';
import { useState, useEffect } from 'react';
import httpClient from '../../api/httpClient';

interface Unit {
  id: number;
  name: string;
}

const CreateUnit = () => {
  const [loading, setLoading] = useState(false);
  const [units, setUnits] = useState<Unit[]>([]);
  const [form] = Form.useForm();

  const columns = [
    {
      title: 'Название',
      dataIndex: 'name',
      key: 'name',
    }
  ];

  const fetchUnits = async () => {
    try {
      const { data } = await httpClient.get('/units');
      setUnits(Array.isArray(data) ? data : data.items || []);
    } catch (error) {
      console.error('Error fetching units:', error);
      message.error('Ошибка при загрузке подразделений');
    }
  };

  useEffect(() => {
    fetchUnits();
  }, []);

  const handleSubmit = async (values: { name: string }) => {
    setLoading(true);
    try {
      await httpClient.put('/units', {
        name: values.name
      });
      message.success('Подразделение успешно создано');
      form.resetFields();
      await fetchUnits();
    } catch (error) {
      console.error('Error creating unit:', error);
      message.error('Ошибка при создании подразделения');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <Card title="Создание нового подразделения" style={{ marginBottom: 20 }}>
        <Form
          form={form}
          layout="vertical"
          onFinish={handleSubmit}
        >
          <Form.Item
            name="name"
            label="Название подразделения"
            rules={[{ required: true, message: 'Введите название подразделения' }]}
          >
            <Input placeholder="Например: Кафедра информатики" />
          </Form.Item>

          <Button
            type="primary"
            htmlType="submit"
            loading={loading}
          >
            Создать подразделение
          </Button>
        </Form>
      </Card>

      <Card title="Существующие подразделения">
        <Table
          columns={columns}
          dataSource={units}
          rowKey="id"
          pagination={{
            pageSize: 10,
            showSizeChanger: true,
            showTotal: (total) => `Всего ${total} подразделений`
          }}
        />
      </Card>
    </div>
  );
};

export default CreateUnit;
