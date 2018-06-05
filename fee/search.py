from datetime import datetime
import urllib.parse as urlparse
from bs4 import BeautifulSoup, UnicodeDammit
import requests


class Search:
    """
    """
    DEFAULT_STAT_URL = ('http://www.belstat.gov.by/ofitsialnaya-statistika/'
                        'solialnaya-sfera/trud/operativnaya-informatsiya_8/'
                        'o-nachislennoi-srednei-zarabotnoi-plate-rabotnikov/')
    DEFAULT_STAT_KEY = ('информационные технологии и деятельность '
                        'в области информационного обслуживания')
    DEFAULT_STAT_PERCENT_URL = ('http://www.belstat.gov.by/'
                                'ofitsialnaya-statistika/'
                                'makroekonomika-i-okruzhayushchaya-sreda/'
                                'tseny/godovye-dannye_3/'
                                'indeksy-tsen-i-tarifov/')
    DEFAULT_STAT_PERCENT_KEY = 'Индекс потребительских цен'
    DEFAULT_STAT_YEAR = datetime.now().year - 1

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
            if '{} {} '.format(m, self.stat_year) in self._text(bs4_a):
                href = bs4_a.get('href')

                if href:
                    yield(href)

    def _month_value(self, link):
        """
        """
        r = self._connection('{}{}'.format(self.domain, link))

        for tr in r.find_all('tr'):
            if tr.td and self._text(tr.td) == self.stat_key:
                for td in tr.find_all('td'):
                    if self._text(td) == self.stat_key:
                        continue

                    self.stat_values.append(self._float(td))

                    break

    def _months_list(self):
        """
        """
        r = self._connection(self.stat_url)
        r = r.find('div', class_='catalogue')

        for li in r.find_all('li'):
            if li.a:
                for link in self._months_links(bs4_a=li.a):
                    self._month_value(link)

    def _stat_percent(self):
        """
        """
        r = self._connection(self.stat_percent_url)
        r = r.find('table', class_='autotbl nohead')

        i = None
        i_year = None
        str_year = str(self.stat_year)
        is_key_year = False

        for tr in r.find_all('tr'):
            for th in tr.find_all('th'):
                if i is None and not th.p:
                    i = 1
                elif th.p:
                    i += 1

                    if self._text(th.p) == str_year:
                        i_year = str_year

                        continue

            if self.stat_percent is not None or i_year is None:
                continue

            for td in tr.find_all('td'):
                if td.p:
                    if is_key_year:
                        i -= 1

                        if i == 0:
                            i = None
                            i_year = None
                            str_year = None
                            self.stat_percent = self._float(td.p) - 100.0

                            return
                    else:
                        if self._text(td.p) == self.stat_percent_key:
                            is_key_year = True
                            i -= 1

    def __init__(self,
                 stat_url=None,
                 stat_key=None,
                 stat_percent_url=None,
                 stat_percent_key=None,
                 stat_year=None):
        """
        """
        self.stat_url = stat_url
        if not self.stat_url:
            self.stat_url = self.DEFAULT_STAT_URL

        self.stat_key = stat_key
        if not self.stat_key:
            self.stat_key = self.DEFAULT_STAT_KEY

        self.stat_percent_url = stat_percent_url
        if not self.stat_percent_url:
            self.stat_percent_url = self.DEFAULT_STAT_PERCENT_URL

        self.stat_percent_key = stat_percent_key
        if not self.stat_percent_key:
            self.stat_percent_key = self.DEFAULT_STAT_PERCENT_KEY

        self.stat_year = stat_year
        if not self.stat_year:
            self.stat_year = self.DEFAULT_STAT_YEAR

        self.session = requests.Session()
        self.stat_values = []
        self.domain = self._domain(self.stat_url)
        self.stat_percent = None

    def go(self):
        """
        """
        self._months_list()

        if len(self.stat_values) > 0:
            self._stat_percent()
