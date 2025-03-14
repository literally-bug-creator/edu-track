import { Card, Form, Input, Select, Button, message, Table } from 'antd';
import { useState, useEffect } from 'react';
import httpClient from '../../api/httpClient';

interface Track {
  id: number;
  name: string;
}

interface Group {
  id: number;
  number: string;
  track_id: number;
  track_name: string;
  created_at: string;
}

const CreateGroup = () => {
  const [tracks, setTracks] = useState<Track[]>([]);
  const [existingGroups, setExistingGroups] = useState<Group[]>([]);
  const [loading, setLoading] = useState(false);
  const [form] = Form.useForm();

  const columns = [
    {
      title: 'Номер группы',
      dataIndex: 'number',
      key: 'number',
    },
    {
      title: 'Направление',
      dataIndex: 'track_name',
      key: 'track_name',
    }
  ];

  const fetchExistingGroups = async () => {
    try {
      const { data } = await httpClient.get('/groups');
      const groups = Array.isArray(data) ? data : data.items || [];
      
      const formattedGroups = await Promise.all(groups.map(async group => {
        try {
          const trackResponse = await httpClient.get(`/tracks/${group.track_id}`);
          return {
            ...group,
            track_name: trackResponse.data.item.name
          };
        } catch (error) {
          console.error(`Error fetching track info for group ${group.id}:`, error);
          return {
            ...group,
            track_name: 'Не указано'
          };
        }
      }));
      
      setExistingGroups(formattedGroups);
    } catch (error) {
      console.error('Error fetching existing groups:', error);
      message.error('Ошибка при загрузке групп');
    }
  };

  useEffect(() => {
    const fetchTracks = async () => {
      try {
        const { data } = await httpClient.get('/tracks');
        setTracks(Array.isArray(data) ? data : data.items || []);
      } catch (error) {
        console.error('Error fetching tracks:', error);
        message.error('Ошибка при загрузке направлений');
      }
    };

    fetchTracks();
    fetchExistingGroups();
  }, []);

  const handleSubmit = async (values: { number: string; track_id: number }) => {
    setLoading(true);
    try {
      await httpClient.put('/groups', {
        number: values.number,
        track_id: values.track_id
      });
      message.success('Группа успешно создана');
      form.resetFields();
      await fetchExistingGroups();
    } catch (error) {
      console.error('Error creating group:', error);
      message.error('Ошибка при создании группы');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <Card title="Создание новой группы" style={{ marginBottom: 20 }}>
        <Form
          form={form}
          layout="vertical"
          onFinish={handleSubmit}
        >
          <Form.Item
            name="number"
            label="Номер группы"
            rules={[{ required: true, message: 'Введите номер группы' }]}
          >
            <Input placeholder="Например: 101" />
          </Form.Item>

          <Form.Item
            name="track_id"
            label="Направление"
            rules={[{ required: true, message: 'Выберите направление' }]}
          >
            <Select
              placeholder="Выберите направление"
              options={tracks.map(track => ({
                value: track.id,
                label: track.name
              }))}
              loading={loading}
            />
          </Form.Item>

          <Button
            type="primary"
            htmlType="submit"
            loading={loading}
          >
            Создать группу
          </Button>
        </Form>
      </Card>

      <Card title="Существующие группы">
        <Table
          columns={columns}
          dataSource={existingGroups}
          rowKey="id"
          pagination={{
            pageSize: 10,
            showSizeChanger: true,
            showTotal: (total) => `Всего ${total} групп`
          }}
        />
      </Card>
    </div>
  );
};

export default CreateGroup;
