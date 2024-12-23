# Generated by Django 5.1.3 on 2024-11-28 15:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField(help_text='The full text of the terms and conditions')),
                ('version', models.CharField(default='1.0', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('effective_date', models.DateField(help_text='The date from which the terms are effective')),
                ('accepted_by_user', models.BooleanField(default=False)),
                ('url', models.URLField(blank=True, help_text='URL for full terms document if hosted externally', null=True)),
                ('privacy_policy_link', models.URLField(blank=True, null=True)),
                ('cookies_policy_link', models.URLField(blank=True, null=True)),
                ('governing_law', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terms_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Terms and Conditions',
                'verbose_name_plural': 'Terms and Conditions',
                'ordering': ['-created_at'],
            },
        ),
    ]
