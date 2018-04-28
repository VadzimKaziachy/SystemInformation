import os
import socket
import logging.config
from models import PCInfo
from models import MetricInfo
from settings.logging import LOGGING_CONFIG
from metrics.cpu_metric import CPUmetric
from metrics.disk_metric import Diskmetric
from metrics.memory_metric import RAMmetric
from metrics.network_metric import Networkmetric
import subprocess

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger('app')


def main():
    logger.info('Started')

    if not PCInfo.select().where(PCInfo.name == os.uname().nodename.lower()):
        obj = PCInfo(name=os.uname().nodename, ip_address=get_ip())
        obj.save()

    logger.info('Finished')


def set_system_info():
    memory = RAMmetric()
    disk = Diskmetric()
    network = Networkmetric()
    cpu = CPUmetric()

    memory.retrieve()
    disk.retrieve()
    network.retrieve()
    cpu.retrieve()

    list_metric = []

    list_metric.append(memory.parse_results())
    list_metric.append(disk.parse_results())
    list_metric.append(network.parse_results())
    list_metric.append(cpu.parse_results())

    for metric in list_metric:
        for i in metric:
            obj = MetricInfo(name=i.name, value=i.value, time=i.time)
            obj.save()


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
    # main()
    # set_system_info()

    a = subprocess.check_output(['mpstat']).decode('utf-8')
    # print(a)

    line1 = []
    line2 = []
    line3 = []

    for i in a.splitlines():
        line1.append(i)

    print(line1[2])
    print(line1[3])
    line2 = line1[2].split('%')
    line3 = line1[3].split(' ')
    print(line2)
    print(line3)