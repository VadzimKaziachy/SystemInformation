import psutil
from metrics.base_metric import Metric
from models import MetricInfo
from datetime import datetime


class CPUmetric(Metric):

    def __init__(self):
        super(CPUmetric, self).__init__(type='cpu')

    def retrieve(self):
        self._data = psutil.cpu_times_percent(interval=1, percpu=False)
        self._time = datetime.now().strftime('%s')

    def parse_results(self):
        result = []
        # print(self._data.__len__())
        # print(self._data)
        # for i in self._data:
        #     print('=========')
        #     for a in i._fields:
        #         print(a)

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
