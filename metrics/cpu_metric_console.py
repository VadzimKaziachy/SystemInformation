from metrics.base_metric import Metric
from models import MetricInfo
from datetime import datetime
from re import findall
from subprocess import check_output


class CPUMetricConsole(Metric):

    def __init__(self):
        super(CPUMetricConsole, self).__init__(type='cpu')

    def retrieve(self):
        self._data = check_output(['mpstat']).decode('utf-8').splitlines()
        self._time = datetime.now().strftime('%s')

    def parse_results(self):
        result = []

        title = findall(r'\w+', self._data[2])[4:]
        value_data = findall(r'\d{,9},\d{,9}', self._data[3])

        for field in title:
            metric = MetricInfo(
                name=self.generate_name(field),
                value=value_data[title.index(field)],
                time=self._time
            )
            result.append(metric)
        return result

    def generate_name(self, field):
        return '.'.join([self._type, field])
