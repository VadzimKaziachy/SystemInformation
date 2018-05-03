import psutil
from metrics.base_metric import Metric
from models import MetricInfo
from datetime import datetime


class NetworkMetric(Metric):

    def __init__(self):
        super(NetworkMetric, self).__init__(type='network')

    def retrieve(self):
        self._data = psutil.net_io_counters(pernic=False)
        self._time = datetime.now().strftime('%s')

    def parse_results(self):
        result = []

        for field in self._data._fields:
            metricInfo = MetricInfo(
                name=self.generate_name(field),
                value=str(getattr(self._data, field)),
                time=self._time
            )
            result.append(metricInfo)

        return result

    def generate_name(self, field):
        return '.'.join([self._type, field])
