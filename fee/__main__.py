from fee.env import Env
from fee.build import Build
from fee.search import Search


def fee():
    """
    """
    env = Env()

    Build(values=Search(url=env.url,
                        key=env.key,
                        year=env.year).go(),
          percent=env.percent,
          filename=env.filename).go()


fee()
