from itertools import chain

from facebook_scraper import get_posts

from constants import Constants

class Scraper:
    def __init__(self):
        self.constants = Constants()

    def run(self, page):
            return get_posts(page, pages=self.constants.get('page_n'))
