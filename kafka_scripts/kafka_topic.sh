#!/usr/bin/env bash
kafka-topics.sh --create --topic facebook_news_posts --zookeeper localhost:2181 --partitions 3 --replication-factor 1