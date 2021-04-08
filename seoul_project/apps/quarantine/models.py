from django.db import models
import uuid
from django.utils import timezone


class Quarantine(models.Model):
    uuid = models.CharField(max_length=36,
                            primary_key=True, default=uuid.uuid4, editable=False)
    first_test = models.CharField(max_length=20, default='untested')
    second_test = models.CharField(max_length=20, default='untested')
    status = models.CharField(max_length=20, default='outOfKorea')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Quarantine'

    def __str__(self):
        return f'{self.uuid}'
