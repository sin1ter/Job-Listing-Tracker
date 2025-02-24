# Generated by Django 5.0.7 on 2024-07-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=254)),
                ('requirements', models.TextField()),
                ('job_position', models.CharField(max_length=254)),
                ('job_link', models.URLField()),
                ('apply_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiters_name', models.CharField(max_length=254)),
                ('recruiters_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=254)),
            ],
        ),
    ]
