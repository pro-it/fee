from fee.env import Env
from fee.search import Search


def fee_search():
    """
    """
    _env = Env()

    Search(month=_env.month,
           year=_env.year,
           key=_env.key).go()


fee_search()
