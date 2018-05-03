import os
import socket
import logging.config
from models import PCInfo
from models import MetricInfo
from settings.logging import LOGGING_CONFIG
from metrics.cpu_metric import CPUMetric
from metrics.disk_metric import DiskMetric
from metrics.ram_metric import RAMMetric
from metrics.network_metric import NetworkMetric
from metrics.cpu_metric_console import CPUMetricConsole
from metrics.disk_metric_console import DiskMetricConsole
from metrics.ram_metric_console import RAMMetricConsole

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger('app')


def main():
    pc_info = init_pc()
    metrics = collect_metrics()
    insert_metrics(metrics=metrics, pc_info=pc_info)


def init_pc():
    logger.info('Started system_name')

    if not PCInfo.select().where(PCInfo.name == os.uname().nodename.lower()):
        obj = PCInfo(name=os.uname().nodename, ip_address=get_ip())
        obj.save()

    logger.info('Finished system_name')

    return PCInfo.select().where(PCInfo.name == os.uname().nodename.lower()).get()


def collect_metrics():
    logger.info('Started collect_metrics')

    memory_metric = RAMMetric()
    disk_metric = DiskMetric()
    network_metric = NetworkMetric()
    cpu_metric = CPUMetric()

    memory_metric.retrieve()
    disk_metric.retrieve()
    network_metric.retrieve()
    cpu_metric.retrieve()

    metrics = []
    metrics.extend(memory_metric.parse_results())
    metrics.extend(disk_metric.parse_results())
    metrics.extend(network_metric.parse_results())
    metrics.extend(cpu_metric.parse_results())

    logger.info('Finished collect_metrics')

    return metrics


def insert_metrics(metrics, pc_info):
    logger.info('Started insert_metrics')
    metrics_db = ({MetricInfo.pc_info: pc_info, MetricInfo.name: metric.name, MetricInfo.value: metric.value,
                   MetricInfo.time: metric.time} for metric in metrics)
    MetricInfo.insert_many(metrics_db).execute()
    logger.info('Finished insert_metrics')


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == '__main__':
    main()

    # memory_metric = RAMMetricConsole()
    # disk_metric = DiskMetricConsole()
    # cpu_metric = CPUMetricConsole()
    #
    # memory_metric.retrieve()
    # disk_metric.retrieve()
    # cpu_metric.retrieve()
    #
    # print(memory_metric.parse_results())
    # print(disk_metric.parse_results())
    # print(cpu_metric.parse_results())
