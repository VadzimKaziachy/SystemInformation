import time
import psutil
from metrics.base_metric import Metric
from models import MetricInfo


class CPUMetric(Metric):

    def __init__(self):
        super(CPUMetric, self).__init__(type='CPUmetric metric')

    def retrieve(self):
        self._data = psutil.cpu_times_percent(interval=1, percpu=False)
        self._time = time.asctime()

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
                name=self._type,
                value='{type} : {filed} : {value}'.format(type=self._type, filed=field,
                                                          value=str(getattr(self._data, field))),
                time=self._time
            )
            result.append(metricInfo)

        return result
