# Generated by Django 3.1.7 on 2021-07-14 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20210715_0412'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='country',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='taluka',
            old_name='country',
            new_name='city',
        ),
    ]
