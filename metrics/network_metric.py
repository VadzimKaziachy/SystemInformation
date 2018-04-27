import time
import psutil
from metrics.base_metric import Metric
from models import MetricInfo


class Network(Metric):

    def __init__(self):
        super(Network, self).__init__(type='Network metric')

    def retrieve(self):
        self._data = psutil.net_io_counters(pernic=False)
        self._time = time.asctime()

    def parse_results(self):
        result = []

        for field in self._data._fields:
            metric = MetricInfo(
                name=self._type,
                value=str(getattr(self._data, field)),
                time=self._time
            )
            result.append(metric)

        return result
