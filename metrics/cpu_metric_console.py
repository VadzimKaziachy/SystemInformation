from metrics.base_metric import Metric
from models import MetricInfo
import subprocess
from datetime import datetime


class CPUmetricConsole(Metric):

    def __init__(self):
        super(CPUmetricConsole, self).__init__(type='cpu')

    def retrieve(self):
        self._data = subprocess.check_output(['cat', '/proc/cpuinfo']).decode('utf-8')
        self._time = datetime.now().strftime('%s')

    def parse_results(self):
        result = []

        for line in self._data.splitlines():
            date_line = line.split(':')
            metric = MetricInfo(
                name=self.generate_name(date_line[0]),
                value=date_line[1],
                time=self._time

            )
            result.append(metric)
        return result

    def generate_name(self, field):
        return '.'.join([self._type, field])
