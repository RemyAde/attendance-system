# Generated by Django 4.1.1 on 2022-09-22 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_customuser_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="subject",),
    ]
