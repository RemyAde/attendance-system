# Generated by Django 4.1.1 on 2022-09-21 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0005_attendance_subject"),
    ]

    operations = [
        migrations.RemoveField(model_name="attendance", name="subject",),
    ]
