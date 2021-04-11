from django.db import models
import uuid
from apps.address.models import Address
from apps.country.models import Country
from apps.university.models import University
from apps.quarantine.models import Quarantine
from django.utils import timezone


class Student(models.Model):
    uuid = models.CharField(max_length=36,
                            primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    kakao_id = models.CharField(max_length=50, blank=True, null=True)
    current_location = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    arrival_date_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, blank=True, null=True, related_name='student_address')
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='student_country')
    quarantine = models.OneToOneField(
        Quarantine, on_delete=models.CASCADE, related_name='student_quarantine', blank=True, null=True)
    university = models.ForeignKey(
        University, on_delete=models.CASCADE, related_name='student_university')

    class Meta:
        db_table = 'Student'

    def __str__(self):
        return f'{self.email}'
