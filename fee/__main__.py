from fee.env import Env
from fee.search import Search


def fee_search():
    """
    """
    _env = Env()

    Search(month=_env.month,
           year=_env.year,
           key=_env.key,
           url=_env.url).go()


fee_search()
