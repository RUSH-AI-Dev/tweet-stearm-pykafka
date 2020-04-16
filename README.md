## tweet-stearm-pykafka
>
>
>
To Run
- start zookeeper
>$KAFKA_HOME/bin/zookeeper-server-start.sh config/zookeeper.properties

- start kafka server
>$KAFKA_HOME/bin/kafka-server-start.sh config/server.properties

- create kafka topics
>$KAFKA_HOME/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test_topic
