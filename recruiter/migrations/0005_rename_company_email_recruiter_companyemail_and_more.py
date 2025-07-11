# Generated by Django 5.1.9 on 2025-06-09 07:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0004_alter_recruiter_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruiter',
            old_name='company_email',
            new_name='companyEmail',
        ),
        migrations.RenameField(
            model_name='recruiter',
            old_name='company_logo',
            new_name='companyLogo',
        ),
        migrations.RenameField(
            model_name='recruiter',
            old_name='company_name',
            new_name='companyName',
        ),
        migrations.RenameField(
            model_name='recruiter',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='recruiter',
            old_name='is_verified',
            new_name='isVerified',
        ),
        migrations.RenameField(
            model_name='recruiter',
            old_name='updated_at',
            new_name='updatedAt',
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='recruiter',
            name='contactInfo',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='user',
            field=models.ForeignKey(blank=True, db_column='users_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruiters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='industry',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
