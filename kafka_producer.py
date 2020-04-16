from pykafka import KafkaClient
import json

client = KafkaClient(hosts='localhost:9092')
topic = client.topics['test_topic']
producer = topic.get_sync_producer()

producer.produce(json.dumps({'created_at': 'Thu Apr 16 02:58:39 2020', 'screen_name': 'palittmorn', 'RT': 'OSW_ONG_ONG', 'text': 'RT @OSW_ONG_ONG: Mask ผ้าฝ้ายมัสลิน สินค้าจากโรงงานผลิตเองค่ะ แบบมีที่ใส่ใส้กรอง ซักได้มากถึง 100 ครั้ง  ผ่านการเทสละอองน้ำแล้ว \nมี 3 ส'}).encode('utf-8'))
