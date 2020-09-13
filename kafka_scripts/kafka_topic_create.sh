#!/usr/bin/env bash
kafka-topics.sh --create --topic facebook_news_posts --zookeeper localhost:2181 --partitions 6 --replication-factor 1
