import psutil
from metrics.base_metric import Metric
from models import MetricInfo
from datetime import datetime


class CPUmetric(Metric):

    def __init__(self):
        super(CPUmetric, self).__init__(type='cpu')

    def retrieve(self):
        self._data = psutil.cpu_times_percent(interval=1, percpu=True)
        self._time = datetime.now().strftime('%s')

    def parse_results(self):
        result = []

        if isinstance(self._data, tuple):
            self._data = [self._data]

        for obj in self._data:
            for field in obj._fields:
                metricInfo = MetricInfo(
                    name=self.generate_name(field, str(self._data.index(obj)+1)),
                    value=str(getattr(obj, field)),
                    time=self._time
                )
                result.append(metricInfo)

        return result

    def generate_name(self, field, core):
        return '.'.join([self._type, core, field])
