# Generated by Django 3.1.7 on 2021-04-08 18:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quarantine', '0001_initial'),
        ('country', '0001_initial'),
        ('address', '0001_initial'),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('kakao_id', models.CharField(blank=True, max_length=50, null=True)),
                ('current_location', models.TextField(blank=True, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('arrival_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_address', to='address.address')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_country', to='country.country')),
                ('quarantine', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_quarantine', to='quarantine.quarantine')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_university', to='university.university')),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
