# Generated by Django 4.1.1 on 2022-09-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="date_completed",
            field=models.DateField(blank=True, null=True),
        ),
    ]
