from fee.env import Env
from fee.build import Build
from fee.search import Search


def fee():
    """
    """
    env = Env()

    search = Search(stat_url=env.stat_url,
                    stat_key=env.stat_key,
                    stat_percent_url=env.stat_percent_url,
                    year=env.year)
    search.go()

    Build(stat_values=search.stat_values,
          stat_percent=search.stat_percent,
          percent=env.percent,
          filename=env.filename).go()


fee()
