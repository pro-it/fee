from fee.env import Env
from fee.build import Build
from fee.search import Search


def fee():
    """
    """
    _env = Env()

    results = Search(url=_env.url,
                     key=_env.key,
                     year=_env.year).go()

    Build(values=results,
          percent=_env.percent,
          filename=_env.filename).go()


fee()
