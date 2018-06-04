
class Build:
    """
    """

    DEFAULT_PERCENT = 20.0

    def __init__(self, values, percent=None, filename=None):
        """
        """
        self.filename = filename
        self.values = values

        self.percent = percent
        if not self.percent:
            self.percent = self.DEFAULT_PERCENT

    def go(self):
        """
        """
