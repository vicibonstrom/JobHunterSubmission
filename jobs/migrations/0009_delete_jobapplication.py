# Generated by Django 5.0.6 on 2024-05-17 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_job_due_date_alter_job_posted_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobApplication',
        ),
    ]