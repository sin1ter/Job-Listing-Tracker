# Generated by Django 5.0.7 on 2024-07-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_job_recruiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]