from peewee import *

from settings import database

# import settings.database as settings

db = MySQLDatabase(**database.DB_CONFIG)

class BaseModel(Model):
    class Meta:
        database = db


class PCInfo(BaseModel):
    id = PrimaryKeyField()
    name = CharField(unique=True)
    ip_address = CharField(unique=True)

    class Meta:
        table_name = 'pc_info'

class MetricInfo(BaseModel):
    value = CharField(unique=True, max_length=255)
    name = CharField(unique=True)
    time = CharField(unique=True)

    class Meta:
        table_name ='metric_info'

