# Generated by Django 5.1.3 on 2024-11-28 06:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('farm_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('wallet_address', models.CharField(max_length=255, unique=True)),
                ('crop_name', models.CharField(max_length=255)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('certification_status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('customUser.user',),
        ),
    ]
