# Generated by Django 3.1.7 on 2021-07-17 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20210717_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]
