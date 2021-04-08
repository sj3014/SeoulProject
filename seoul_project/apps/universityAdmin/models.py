from django.db import models
import uuid
from apps.university.models import University
from django.utils import timezone


class UniversityAdmin(models.Model):
    uuid = models.CharField(max_length=36,
                            primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    university = models.ForeignKey(
        University, on_delete=models.CASCADE, related_name='universityAdmin_university')

    class Meta:
        db_table = 'UniversityAdmin'

    def __str__(self):
        return f'{self.email}'
