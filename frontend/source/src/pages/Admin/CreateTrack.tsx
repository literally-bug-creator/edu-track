import { Card, Form, Input, Select, Button, message, Table } from 'antd';
import { useState, useEffect } from 'react';
import httpClient from '../../api/httpClient';

interface Unit {
  id: number;
  name: string;
}

interface Track {
  id: number;
  name: string;
  unit_name: string;
  unit_id: number;
}

const CreateTrack = () => {
  const [tracks, setTracks] = useState<Track[]>([]);
  const [units, setUnits] = useState<Unit[]>([]);
  const [loading, setLoading] = useState(false);
  const [form] = Form.useForm();

  const columns = [
    {
      title: 'Название',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Подразделение',
      dataIndex: 'unit_name',
      key: 'unit_name',
    }
  ];

  const fetchExistingTracks = async () => {
    try {
      const { data } = await httpClient.get('/tracks');
      const tracks = Array.isArray(data) ? data : data.items || [];
      
      const formattedTracks = await Promise.all(tracks.map(async (track: Track) => {
        try {
          const unitResponse = await httpClient.get(`/units/${track.unit_id}`);
          return {
            ...track,
            unit_name: unitResponse.data.item.name
          };
        } catch (error) {
          console.error(`Error fetching unit info for track ${track.id}:`, error);
          return {
            ...track,
            unit_name: 'Не указано'
          };
        }
      }));
      
      setTracks(formattedTracks);
    } catch (error) {
      console.error('Error fetching existing tracks:', error);
      message.error('Ошибка при загрузке направлений');
    }
  };

  useEffect(() => {
    const fetchUnits = async () => {
      try {
        const { data } = await httpClient.get('/units');
        setUnits(Array.isArray(data) ? data : data.items || []);
      } catch (error) {
        console.error('Error fetching units:', error);
        message.error('Ошибка при загрузке подразделений');
      }
    };

    fetchUnits();
    fetchExistingTracks();
  }, []);

  const handleSubmit = async (values: { name: string; unit_id: number }) => {
    setLoading(true);
    try {
      await httpClient.put('/tracks', {
        name: values.name,
        unit_id: values.unit_id
      });
      message.success('Направление успешно создано');
      form.resetFields();
      await fetchExistingTracks();
    } catch (error) {
      console.error('Error creating track:', error);
      message.error('Ошибка при создании направления');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <Card title="Создание нового направления" style={{ marginBottom: 20 }}>
        <Form
          form={form}
          layout="vertical"
          onFinish={handleSubmit}
        >
          <Form.Item
            name="name"
            label="Название направления"
            rules={[{ required: true, message: 'Введите название направления' }]}
          >
            <Input placeholder="Например: Прикладная математика и информатика" />
          </Form.Item>

          <Form.Item
            name="unit_id"
            label="Подразделение"
            rules={[{ required: true, message: 'Выберите подразделение' }]}
          >
            <Select
              placeholder="Выберите подразделение"
              options={units.map(unit => ({
                value: unit.id,
                label: unit.name
              }))}
              loading={loading}
            />
          </Form.Item>

          <Button
            type="primary"
            htmlType="submit"
            loading={loading}
          >
            Создать направление
          </Button>
        </Form>
      </Card>

      <Card title="Существующие направления">
        <Table
          columns={columns}
          dataSource={tracks}
          rowKey="id"
          pagination={{
            pageSize: 10,
            showSizeChanger: true,
            showTotal: (total) => `Всего ${total} направлений`
          }}
        />
      </Card>
    </div>
  );
};

export default CreateTrack;
