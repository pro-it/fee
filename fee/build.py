

class Build:
    """
    """

    DEFAULT_PERCENT = 20.0

    def _build(self, length):
        """
        """
        if length > 0:
            self.value = int(sum(self.values)/length*
                             0.01*
                             (100 + self.percent)/100.0)

    def _file_create(self):
        """
         Create file if file name defined
        """
        if self.filename:
            with open(self.filename, 'w') as f:
                f.write(str(self.value))
                f.close()

    def __init__(self, values, percent=None, filename=None):
        """
        """
        self.filename = filename
        self.values = values
        self.value = 0

        self.percent = percent
        if self.percent is None:
            self.percent = self.DEFAULT_PERCENT

    def go(self):
        """
        """
        self._build(length=len(self.values))
        self._file_create()