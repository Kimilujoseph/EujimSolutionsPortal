# Generated by Django 4.2.21 on 2025-07-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0016_remove_recruitertracking_unique_job_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitertracking',
            name='interviewDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
