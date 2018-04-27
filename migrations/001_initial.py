import datetime as dt
import peewee as pw

def migrate(migrator, database, **kwargs):


    @migrator.create_model
    class PCInfo(pw.Model):
        id = pw.PrimaryKeyField()
        name = pw.CharField(unique=True)
        ip = pw.CharField(unique=True)


def rollback(migrator, database, fake=False, **kwargs):
    pass
