import os


class Env:
    """
    """

    VARS = [
        'PROIT_FEE_URL',
        'PROIT_FEE_KEY',
        'PROIT_FEE_YEAR',
        'PROIT_FEE_MONTH'
    ]

    CONFIG_FILE = './.env'

    def __init__(self):
        """
        Initialization variables
        """
        # PROIT_FEE_URL
        self.url = os.getenv(self.VARS[0], None)

        # PROIT_FEE_KEY
        self.key = os.getenv(self.VARS[1], None)

        # PROIT_FEE_YEAR
        self.year = os.getenv(self.VARS[2], None)

        # PROIT_FEE_MONTH
        self.month = os.getenv(self.VARS[3], None)
