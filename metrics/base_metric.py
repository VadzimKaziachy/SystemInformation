from datetime import datetime

class Metric:

    def __init__(self, type):
        self._type = type

    def retrieve(self):
        raise NotImplemented

    def parse_results(self):
        raise NotImplemented