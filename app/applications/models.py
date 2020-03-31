import uuid

from django.db import models


class Application(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    access_key = models.UUIDField(verbose_name='Access Key',
                                  default=uuid.uuid4,
                                  editable=False,
                                  unique=True,
                                  db_index=True)

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
