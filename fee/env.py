import os


class Env:
    """
    """

    VARS = [
        'PRGIT_FEE_STAT_URL',
        'PRGIT_FEE_STAT_KEY',
        'PRGIT_FEE_STAT_PERCENT_URL',
        'PRGIT_FEE_STAT_PERCENT_KEY',
        'PRGIT_FEE_STAT_YEAR',
        'PRGIT_FEE_PERCENT',
        'PRGIT_FEE_FILE'
    ]

    CONFIG_FILE = './.env'

    def __init__(self):
        """
        Initialization variables
        """
        # PRGIT_FEE_STAT_URL
        self.stat_url = os.getenv(self.VARS[0], None)

        # PRGIT_FEE_STAT_KEY
        self.stat_key = os.getenv(self.VARS[1], None)

        # PRGIT_FEE_STAT_PERCENT_URL
        self.stat_percent_url = os.getenv(self.VARS[2], None)

        # PRGIT_FEE_STAT_PERCENT_KEY
        self.stat_percent_key = os.getenv(self.VARS[3], None)

        # PRGIT_FEE_STAT_YEAR
        self.stat_year = os.getenv(self.VARS[4], None)
        if self.stat_year:
            self.stat_year = int(self.stat_year)

        # PRGIT_FEE_PERCENT
        self.percent = os.getenv(self.VARS[5], None)
        if self.percent:
            self.percent = float(self.percent)

        # PRGIT_FEE_FILE
        self.filename = os.getenv(self.VARS[6], None)
