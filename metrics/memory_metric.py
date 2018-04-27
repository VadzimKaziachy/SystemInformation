import time
import psutil
from metrics.base_metric import Metric
from models import MetricInfo


class Memory(Metric):

    def __init__(self):
        super(Memory, self).__init__(type='Memory metric')

    def retrieve(self):
        self._data = psutil.virtual_memory()
        self._time = time.asctime()

    def parse_results(self):
        result = []

        for field in self._data._fields:
            metricInfo = MetricInfo(
                name=self._type,
                value=str(getattr(self._data, field)),
                time=self._time
            )
            result.append(metricInfo)

        return result
