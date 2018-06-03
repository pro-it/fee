from fee.env import Env
from fee.build import Build
from fee.search import Search


def fee():
    """
    """
    _env = Env()

    Search(url=_env.url,
           key=_env.key,
           year=_env.year,
           month=_env.month).go()

    Build(None).go


fee()
