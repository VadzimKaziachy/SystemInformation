import psutil
from metrics.base_metric import Metric
from models import MetricInfo
from datetime import datetime
from re import findall
from subprocess import check_output


class RAMMetricConsole(Metric):

    def __init__(self):
        super(RAMMetricConsole, self).__init__(type='ram')

    def retrieve(self):
        self._data = check_output(['free', '-wb']).decode('utf-8').splitlines()
        self._time = datetime.now().strftime('%s')

    def parse_results(self):
        result = []

        title = findall(r'\w+', self._data[0])
        value_data = findall(r'\d+', self._data[1])

        if title.__len__() == value_data.__len__():
            for field in title:
                metricInfo = MetricInfo(
                    name=self.generate_name(field),
                    value=value_data[title.index(field)],
                    time=self._time,
                )
                result.append(metricInfo)
        return result

    def generate_name(self, field):
        return '.'.join([self._type, field])
