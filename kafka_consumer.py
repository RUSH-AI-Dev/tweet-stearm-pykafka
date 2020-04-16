#%%
from pykafka import KafkaClient
from pykafka.common import OffsetType
import json
client = KafkaClient(hosts='localhost:9092')
print(client.topics)
#%%
consumer = client.topics['test_topic'].get_simple_consumer(auto_offset_reset=OffsetType.LATEST, reset_offset_on_start=True)
#%%
for msg in consumer:
    print(json.loads(msg.value)['text'])
