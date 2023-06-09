# Generated by Django 4.2b1 on 2023-03-31 23:36

from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations


def create_admin(apps, schema_editor):
    User.objects.create_superuser("admin", password=settings.ADMIN_PASS)


class Migration(migrations.Migration):
    dependencies = [
        ("businesses", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_admin)]
