# Generated by Django 5.1 on 2024-08-18 14:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="ethereum_address",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="private_key",
        ),
    ]
