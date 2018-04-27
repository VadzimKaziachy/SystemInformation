import peewee as pw

def migrate(migrator, database, **kwargs):


    @migrator.create_model
    class MetricInfo(pw.Model):
        value = pw.CharField(unique=True, max_length=255)
        name = pw.CharField(unique=True)
        time = pw.CharField(unique=True)


def rollback(migrator, database, fake=False, **kwargs):
    pass