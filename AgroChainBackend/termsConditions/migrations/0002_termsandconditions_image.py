# Generated by Django 5.1.3 on 2024-11-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termsConditions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='termsandconditions',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload a full image of the product', null=True, upload_to='termsConditions_images/'),
        ),
    ]
