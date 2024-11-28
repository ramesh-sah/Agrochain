# Generated by Django 5.1.3 on 2024-11-28 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0001_initial'),
        ('retailer', '0001_initial'),
        ('smartContract', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smartcontract',
            options={'ordering': ['-created_at'], 'verbose_name': 'Smart Contract', 'verbose_name_plural': 'Smart Contracts'},
        ),
        migrations.AddField(
            model_name='smartcontract',
            name='customer_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='smartcontract',
            name='distributor_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='smartcontract',
            name='farmer_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='smartcontract',
            name='initiator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initiated_contracts', to='distributor.distributor'),
        ),
        migrations.AlterField(
            model_name='smartcontract',
            name='receiver',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_contracts', to='retailer.retailer'),
        ),
    ]