import psutil
from metrics.base_metric import Metric
from datetime import datetime
from models import MetricInfo
from subprocess import check_output
from re import findall
import re


class DiskMetricConsole(Metric):

    def __init__(self):
        super(DiskMetricConsole, self).__init__(type='disk')

    def retrieve(self):
        self._data = check_output(['df','--block-size=1']).decode('utf-8').splitlines()
        self._time = datetime.now().strftime('%s')

    def parse_results(self):
        result = []
        title = ['total', 'used', 'free', 'percent']

        disk_strings = list(filter(lambda x: re.findall(r'\/dev\/sd\w+', x), self._data))
        for i in disk_strings:
            match = re.match(r'(\/dev\/\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', i)

            if match:
                disk_name = re.findall(r'(sdb\w+)', match.group(1))[0]

                for field in title:
                    metricInfo = MetricInfo(
                        name=self.generate_name(disk_name, field),
                        value=match.group(title.index(field) + 2),
                        time=self._time,
                    )
                    result.append(metricInfo)
            else:

                pass

        return result

    def generate_name(self, disk, field):
        return '.'.join([self._type, disk, field])
