import peewee as pw


def migrate(migrator, database, **kwargs):
    @migrator.create_model
    class MetricInfo(pw.Model):
        name = pw.CharField(unique=False)
        value = pw.CharField(unique=False, max_length=255)
        time = pw.CharField(unique=False)


def rollback(migrator, database, fake=False, **kwargs):
    pass
