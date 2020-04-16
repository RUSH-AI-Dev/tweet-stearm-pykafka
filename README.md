## tweet-stearm-pykafka
>
>
>
To Run
- start zookeeper
>$KAFKA_HOME/bin/zookeeper-server-start.bat config/zookeeper.properties

- start kafka server
>$KAFKA_HOME/bin/kafka-server-start.bat config/server.properties

- create kafka topics
>$KAFKA_HOME/bin/kafka-topics.bat --create --zookeeper localhost:9092 --replication-factor 1 --partitions 1 --topic test_topic
