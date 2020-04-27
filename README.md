## tweet-stearm-pykafka
>
>
>
To Run
- start zookeeper
>$KAFKA_HOME/bin/windows/zookeeper-server-start.bat ../../config/zookeeper.properties

- start kafka server
>$KAFKA_HOME/bin/windows/kafka-server-start.bat ../../config/server.properties

- create kafka topics
>$KAFKA_HOME/bin/windows/kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test_topic

- topic describe
>$KAFKA_HOME/kafka-topics.bat --zookeeper localhost:2181 --topic test_topic --describe

- test: producer 
>$KAFKA_HOME/kafka-console-producer.bat --broker-list localhost:9092 --topic test_topic
>>ex:
>>>hello 1
>>>hello 2
>>>hello 3

- test: consumer 
>$KAFKA_HOME/kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test_topic --from-beginning
>>receive:
>>>hello 1
>>>hello 2
>>>hello 3


