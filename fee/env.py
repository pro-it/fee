import os


class Env:
    """
    """

    VARS = [
        'PROIT_FEE_STAT_URL',
        'PROIT_FEE_STAT_KEY',
        'PROIT_FEE_STAT_PERCENT_URL',
        'PROIT_FEE_YEAR',
        'PROIT_FEE_PERCENT',
        'PROIT_FEE_FILE'
    ]

    CONFIG_FILE = './.env'

    def __init__(self):
        """
        Initialization variables
        """
        # PROIT_FEE_STAT_URL
        self.stat_url = os.getenv(self.VARS[0], None)

        # PROIT_FEE_STAT_KEY
        self.stat_key = os.getenv(self.VARS[1], None)

        # PROIT_FEE_STAT_PERCENT_URL
        self.stat_percent_url = os.getenv(self.VARS[2], None)

        # PROIT_FEE_YEAR
        self.year = os.getenv(self.VARS[3], None)
        if self.year:
            self.year = int(self.year)

        # PROIT_FEE_PERCENT
        self.percent = os.getenv(self.VARS[4], None)
        if self.percent:
            self.percent = float(self.percent)

        # PROIT_FEE_FILE
        self.filename = os.getenv(self.VARS[5], None)
