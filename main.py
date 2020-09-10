import logging
# from apscheduler.schedulers.blocking import BlockingScheduler

from constants import Constants
from producer import Producer
from scraper import Scraper

if __name__ == '__main__':
    producer = Producer()
    scraper = Scraper()
    constants = Constants()

    logger = logging.getLogger('kafka-log')
    fileHandler = logging.FileHandler(constants.get('log_file'))
    logger.setLevel(logging.DEBUG)
    fileHandler.setLevel(logging.DEBUG)

    logging.basicConfig(filename=constants.get('log_file'), filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    for post in scraper.run():
        producer.produce_json_data(key=str.encode(post.get('post_id')), data=post)