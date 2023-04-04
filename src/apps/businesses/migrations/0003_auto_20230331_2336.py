# Generated by Django 4.2b1 on 2023-03-31 23:36

from django.db import migrations


def create_ny_state(apps, schema_editor):
    State = apps.get_model("businesses", "State")
    State.objects.create(value="NY")


class Migration(migrations.Migration):
    dependencies = [
        ("businesses", "0002_auto_20230331_2336"),
    ]

    operations = [migrations.RunPython(create_ny_state)]
