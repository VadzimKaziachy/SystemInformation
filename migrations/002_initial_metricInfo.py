import peewee as pw

def migrate(migrator, database, **kwargs):


    @migrator.create_model
    class MetricInfo(pw.Model):
        value = pw.CharField(unique=False, max_length=255)
        name = pw.CharField(unique=False)
        time = pw.CharField(unique=False)


def rollback(migrator, database, fake=False, **kwargs):
    pass