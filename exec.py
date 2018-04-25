import os
import socket
import psutil
import logging.config
from models import db
from models import PCInfo
from models import PCInfoSystem
from settings.logging import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger('app')

def main():

    db.create_tables([PCInfo])
    obj = PCInfo(name=os.uname().nodename, ip=get_ip())
    obj.save()



    logger.info('Started')
    query = PCInfo.select(PCInfo.name, PCInfo.ip)
    [print('{name} : {ip}'.format(name=x.name, ip=x.ip)) for x in query]
    logger.info('Finished')

def set_system_info():
    db.create_tables([PCInfoSystem])
    obj = PCInfoSystem(info=get_CPU(), name=os.uname().nodename)
    obj.save()
    obj = PCInfoSystem(info=get_memory(), name=os.uname().nodename)
    obj.save()
    obj = PCInfoSystem(info=get_disks(), name=os.uname().nodename)
    obj.save()
    obj = PCInfoSystem(info=get_network(), name=os.uname().nodename)
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

def get_CPU():
    return psutil.cpu_times_percent(interval=1, percpu=True)

def get_memory():
    return psutil.virtual_memory()

def get_disks():
    return psutil.disk_usage('/')

def get_network():
    return psutil.net_io_counters(pernic=False)



if __name__ == '__main__':
    # main()
    set_system_info()
