from fee.env import Env
from fee.build import Build
from fee.search import Search


def fee():
    """
    """
    env = Env()

    search = Search(url=env.url,
                    key=env.key,
                    year=env.year,
                    state_url=env.state_url)
    search.go()

    Build(values=search.values,
          stat_percent=search.stat_percent,
          percent=env.percent,
          filename=env.filename).go()


fee()
