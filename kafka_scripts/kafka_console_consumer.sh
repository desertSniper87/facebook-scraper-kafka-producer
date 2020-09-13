#!/usr/bin/env bash
kafka-console-consumer.sh --topic facebook_news_posts --bootstrap-server 127.0.0.1:9092 --from-beginning
# --group my-first-application