from fee.env import Env
from fee.build import Build
from fee.search import Search

import sys
from time import strftime


__all__ = [
    'env',
    'build',
    'search'
]


DATE_FORMAT = '%Y/%m/%d %H:%M:%S'
RRINT_SPACE = '    '

def message(text, end='\n'):
    """
    Common method for print in STDOUT
    """
    sys.stdout.write(text + end)
    sys.stdout.flush()


def error_message(text, cls_name='', end='\n'):
    """
    Common method for print in STDERR
    """
    sys.stderr.write('{} - {} - [ERROR] {}'.format(strftime(DATE_FORMAT),
                                                   cls_name,
                                                   text + end))
    sys.stderr.flush()
