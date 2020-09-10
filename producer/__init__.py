import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

from constants import Constants

from logging import getLogger


class Producer:
    def __init__(self):
        self.constants = Constants()
        self._logger = getLogger('kafka-log')

        self._producer = KafkaProducer(
            bootstrap_servers=[self.constants.get('bootstrapServers')],
            value_serializer=lambda m: json.dumps(m, ensure_ascii=False, default=str).encode('utf8'),
            retries=self.constants.get('kafka_retries') or 0,
        )

    def on_send_success(self, record_metadata):
        self._logger.info('Topic: ' + str(record_metadata.topic))
        self._logger.info('Partition: ' + str(record_metadata.partition))
        self._logger.info('Offset: ' + str(record_metadata.offset))

    def on_send_error(self, exception):
        self._logger.error('Error occured.', exc_info=exception)

    def produce_json_data(self, key, data):
        try:
            self._producer.send(self.constants.get('topic'), key=key, value=data)\
                .add_callback(self.on_send_success)\
                .add_errback(self.on_send_error)

            self._producer.flush()
        except KafkaError as k:
            self._logger.error(k)