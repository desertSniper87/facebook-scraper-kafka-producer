import os


class Constants:
    def __init__(self):
        self._dict = {
            'bootstrapServers': 'localhost:9092',
            'topic': 'facebook_news_posts',
            'log_file': os.path.join(os.getcwd(), 'log/kafka-log.log'),
            'retries': 3,
            'page_names': {
                'Prothom Alo': 'DailyProthomAlo',
                'Somoy TV': 'somoynews.tv'
            },
            'page_n': 5
        }

    def get(self, key):
        return self._dict.get(key)
