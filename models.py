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
    id = PrimaryKeyField
    value = CharField(unique=False, max_length=255, primary_key=False)
    name = CharField(unique=False, primary_key=False)
    time = CharField(unique=False, primary_key=False)

    class Meta:
        table_name ='metric_info'

