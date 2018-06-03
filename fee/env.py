import os


class Env:
    """
    """

    VARS = [
        'PROIT_FEE_MONTH',
        'PROIT_FEE_YEAR',
        'PROIT_FEE_KEY'
    ]

    CONFIG_FILE = './.env'

    def __init__(self):
        """
        Initialization variables
        """
        # PROIT_FEE_MONTH
        self.month = os.getenv(self.VARS[0], None)

        # PROIT_FEE_YEAR
        self.year = os.getenv(self.VARS[1], None)

        # PROIT_FEE_KEY
        self.key = os.getenv(self.VARS[2], None)
