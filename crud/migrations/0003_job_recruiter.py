# Generated by Django 5.0.7 on 2024-07-25 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_skills_options_alter_job_apply_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='recruiter',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud.recruiter'),
            preserve_default=False,
        ),
    ]
