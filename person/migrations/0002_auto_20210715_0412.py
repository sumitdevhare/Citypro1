# Generated by Django 3.1.7 on 2021-07-14 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='City',
            new_name='Taluka',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='city',
            new_name='taluka',
        ),
    ]
