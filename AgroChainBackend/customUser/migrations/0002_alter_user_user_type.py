# Generated by Django 5.1.3 on 2024-11-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('farmer', 'Farmer'), ('customer', 'Customer'), ('retailer', 'Retailer'), ('distributor', 'Distributor'), ('admin', 'Admin')], max_length=20),
        ),
    ]
