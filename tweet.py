#%%
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials
import json 
import pandas as pd
import datetime
import warnings
warnings.filterwarnings("ignore")
import time
from pykafka import KafkaClient

#setup kafka producer
client = KafkaClient(hosts='localhost:9092')
topic = client.topics['test_topic']
producer = topic.get_sync_producer()


class StdOutListener(StreamListener):
    def on_data(self, data):
        data = json.loads(data)
        try:
            d = {'created_at':  time.asctime( time.localtime(time.time()) ), 'screen_name': data['user']['screen_name'],'RT': data['text'].split('@')[1].split(':')[0] ,'text': data['text']}
            data = json.dumps(d)
            producer.produce(data.encode('utf-8'))
            print(d)
        except:
            d = {'created_at':  time.asctime( time.localtime(time.time()) ), 'screen_name': data['user']['screen_name'],'RT': 'Main Node' ,'text': data['text']}
            data = json.dumps(d)
            producer.produce(data.encode('utf-8'))
            print(d)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    auth = OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    listener = StdOutListener()
    Stream = Stream(auth, listener)
    Stream.filter(track=['โควิด19'])

    