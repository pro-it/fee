

class Build:
    """
    """

    DEFAULT_STAT_PERCENT = 0.0
    DEFAULT_PERCENT = 1.0

    MAGIC_ROUNDING_STEP = 5.0

    def _magic_rounding(self):
        """
        """
        magic = self.value/self.MAGIC_ROUNDING_STEP
        magic_i = int(magic)

        if magic != magic_i:
            self.value = int((magic_i + 1)*self.MAGIC_ROUNDING_STEP)

        magic = None
        magic_i = None

    def _build(self, length):
        """
        """
        if length > 0:
            self.value = int(sum(self.stat_values)/length*
                             self.percent/100.0*
                             (100.0 + self.stat_percent)/100.0)
            self._magic_rounding()

    def _file_create(self):
        """
         Create file if file name defined
        """
        if self.filename:
            with open(self.filename, 'w') as f:
                f.write(str(self.value))
                f.close()

    def __init__(self,
                 stat_values,
                 stat_percent=None,
                 percent=None,
                 filename=None):
        """
        """
        self.stat_values = stat_values
        self.filename = filename
        self.value = 0

        self.percent = percent
        if self.percent is None:
            self.percent = self.DEFAULT_PERCENT

        self.stat_percent = stat_percent
        if self.stat_percent is None:
            self.stat_percent = self.DEFAULT_STAT_PERCENT

    def go(self):
        """
        """
        self._build(length=len(self.stat_values))
        self._file_create()
