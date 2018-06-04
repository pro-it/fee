from datetime import datetime


class Search:
    """
    """
    DEFAULT_URL = ('http://www.belstat.gov.by/ofitsialnaya-statistika/'
                   'solialnaya-sfera/trud/operativnaya-informatsiya_8/'
                   'o-nachislennoi-srednei-zarabotnoi-plate-rabotnikov/')
    DEFAULT_KEY = ('информационные технологии и деятельность'
                   ' в области информационного обслуживания')
    DEFAULT_YEAR = datetime.now().year - 1

    MONTH_MAP = [
        'в январе',
        'в феврале',
        'в марте',
        'в апреле',
        'в мае',
        'в июне',
        'в июле',
        'в августе',
        'в сентябре',
        'в октябре',
        'в ноябре',
        'в декабре'
    ]

    def __init__(self, url=None, key=None, year=None):
        """
        """
        self.values = []

        self.url = url
        if not self.url:
            self.url = self.DEFAULT_URL

        self.key = key
        if not self.key:
            self.key = self.DEFAULT_KEY

        self.year = year
        if not self.year:
            self.year = self.DEFAULT_YEAR

    def go(self):
        """
        """
        return self.values
