from datetime import datetime
import urllib.parse as urlparse
from bs4 import BeautifulSoup, UnicodeDammit
import requests


class Search:
    """
    """
    DEFAULT_URL = ('http://www.belstat.gov.by/ofitsialnaya-statistika/'
                   'solialnaya-sfera/trud/operativnaya-informatsiya_8/'
                   'o-nachislennoi-srednei-zarabotnoi-plate-rabotnikov/')
    DEFAULT_KEY = ('информационные технологии и деятельность'
                   ' в области информационного обслуживания')
    DEFAULT_YEAR = datetime.now().year - 1
    DEFAULT_STATE_URL = ('http://www.belstat.gov.by/ofitsialnaya-statistika/'
                         'makroekonomika-i-okruzhayushchaya-sreda/tseny/'
                         'godovye-dannye_3/indeksy-tsen-i-tarifov/')

    # Routing map for months
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

    # Content encoding
    ENCODING = 'utf-8'
    # Parser type of BeautifulSoup
    BS4_PARSER = 'lxml'

    def _domain(self, url):
        """
        """
        return (lambda u: '{}://{}'.format(u.scheme,
                                           u.netloc))(urlparse.urlparse(url))

    def _text(self, res):
        """
        String striping for content
        """
        return res.text.strip().replace('\xc2\xa0', ' ').replace(
            '\xa0', ' ').replace('  ', ' ').replace('\n', ' ').replace(
            '\r', ' ').replace('  ', ' ')

    def _float(self, res):
        """
        """
        return float(self._text(res).replace(',', '.').replace(' ', ''))

    def _beautiful_soup(self, r):
        """ 
        """
        return BeautifulSoup(UnicodeDammit(r.text).unicode_markup,
                             self.BS4_PARSER)

    def _is_valid(self, r):
        """
        Checking HTTP respose status for BeautifulSoup4
        """
        return (r.ok or
                r.status_code == 200 or
                r.status_code == 201 or
                r.status_code == 301 or
                r.status_code == 302)

    def _connection(self, url):
        """
        """
        r = self.session.get(url, timeout=300)

        if self._is_valid(r):
            r = self._beautiful_soup(r)
        else:
            r = None

        return r

    def _months_links(self, bs4_a):
        """
        """
        for m in self.MONTH_MAP:
            if '{} {} '.format(m, self.year) in self._text(bs4_a):
                href = bs4_a.get('href')

                if href:
                    yield(href)

    def _month_value(self, link):
        """
        """
        r = self._connection('{}{}'.format(self.domain, link))

        for tr in r.find_all('tr'):
            if tr.td and self._text(tr.td) == self.key:
                for td in tr.find_all('td'):
                    if self._text(td) == self.key:
                        continue

                    self.values.append(self._float(td))
                    break

    def _months_list(self):
        """
        """
        r = self._connection(self.url)

        for i in r.find_all('div'):
            div = i.get('class')

            if div and div[0] and div[0] == 'catalogue':
                for li in i.find_all('li'):
                    if li.a:
                        for link in self._months_links(bs4_a=li.a):
                            self._month_value(link)
                break

    def _stat_percent(self):
        """
        """

    def __init__(self, url=None, key=None, year=None, state_url=None):
        """
        """
        self.url = url
        if not self.url:
            self.url = self.DEFAULT_URL

        self.key = key
        if not self.key:
            self.key = self.DEFAULT_KEY

        self.year = year
        if not self.year:
            self.year = self.DEFAULT_YEAR

        self.state_url = state_url
        if not self.state_url:
            self.state_url = self.DEFAULT_STATE_URL

        self.session = requests.Session()
        self.values = []
        self.domain = self._domain(self.url)
        self.stat_percent = 0

    def go(self):
        """
        """
        self._months_list()
        self._stat_percent()

        return self.values
