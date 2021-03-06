import psutil
from metrics.base_metric import Metric
from models import MetricInfo
from datetime import datetime


class RAMMetric(Metric):

    def __init__(self):
        super(RAMMetric, self).__init__(type='ram')

    def retrieve(self):
        self._data = psutil.virtual_memory()
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
