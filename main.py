import logging
from apscheduler.schedulers.blocking import BlockingScheduler

from constants import Constants
from producer import Producer
from scraper import Scraper

if __name__ == '__main__':
    producer = Producer()
    scraper = Scraper()
    constants = Constants()

    logger = logging.getLogger('kafka-log')
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler(constants.get('log_file'))
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)

    print("Apache Kafka running on " + constants.get('bootstrapServers') + " With topic name " + constants.get('topic'))

    pages = constants.get('page_names').values()
    def run_scraper():
        for page in pages:
            for post in scraper.run(page):
                producer.produce_json_data(key=str.encode(post.get('post_id')), data=post)


    scheduler = BlockingScheduler()
    for page in pages:
        scheduler.add_job(run_scraper, 'interval', minutes=2)
    scheduler.start()
