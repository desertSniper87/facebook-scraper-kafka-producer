from facebook_scraper import get_posts

from constants import Constants

class Scraper:
    def __init__(self):
        self.constants = Constants()
        self.pages = self.constants.get('page_names').values()

    def run(self):
        for page in (self.pages):
            return get_posts(page, pages=self.constants.get('page_n'))
