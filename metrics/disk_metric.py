import psutil
from metrics.base_metric import Metric
from datetime import datetime
from models import MetricInfo
import re


class DiskMetric(Metric):

    def __init__(self):
        super(DiskMetric, self).__init__(type='disk')

    def retrieve(self):
        self._data = psutil.disk_usage('/')
        self._time = datetime.now().strftime('%s')

    def parse_results(self):
        result = []

        disk_partitions = psutil.disk_partitions()

        hard_drives = list(filter(lambda x: x.device.startswith('/dev/sdb'), disk_partitions))
        for hard_drive in hard_drives:
            disk_name = re.findall(r'(sdb\w+)', hard_drive.device)[0]
            data = psutil.disk_usage(hard_drive.mountpoint)
            for field in data._fields:
                metricInfo = MetricInfo(
                    name=self.generate_name(disk_name, field),
                    value=str(getattr(data, field)),
                    time=self._time
                )
                result.append(metricInfo)

        return result

    def generate_name(self, disk, field):
        return '.'.join([self._type, disk, field])
