# Generated by Django 3.1.7 on 2021-07-18 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0014_person_registration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='registration',
        ),
    ]
