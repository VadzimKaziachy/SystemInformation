import os
import socket
import psutil
import time
import logging.config
from models import PCInfo
from models import MetricInfo
from settings.logging import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger('app')


def main():
    obj = PCInfo(name=os.uname().nodename, ip=get_ip())
    obj.save()

    logger.info('Started')
    query = PCInfo.select(PCInfo.name, PCInfo.ip)
    [print('{name} : {ip}'.format(name=x.name, ip=x.ip)) for x in query]
    logger.info('Finished')


# def set_system_info():

# obj=MetricInfo(name="CPU", value=get_CPU(), time=time.asctime())
# obj.save()
# obj=MetricInfo(name="Memory", value=get_memory(), time=time.asctime())
# obj.save()
# obj=MetricInfo(name='Disks', value=get_disks(), time=time.asctime())
# obj.save()
# obj=MetricInfo(name='Network', value=get_network(), time=time.asctime())
# obj.save()

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


from metrics.CPU_metric import CPUMetric
from metrics.disk_metric import Disk
from metrics.memory_metric import Memory
from metrics.network_metric import Network

if __name__ == '__main__':
    memore = Memory()
    memore.retrieve()
    # print(memore.parse_results())

    # for i in memore.parse_results():
    #     print(i.name + " = "+i.time +' = '+ i.value)

    cpu = CPUMetric()
    cpu.retrieve()
    # cpu.parse_results()
    [print(i.value) for i in cpu.parse_results()]

    # main()
    # set_system_info()
