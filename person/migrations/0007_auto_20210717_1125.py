# Generated by Django 3.1.7 on 2021-07-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20210717_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='addhar',
            field=models.CharField(max_length=15),
        ),
    ]
