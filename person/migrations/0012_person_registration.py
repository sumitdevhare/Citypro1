# Generated by Django 3.1.7 on 2021-07-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0011_auto_20210718_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='registration',
            field=models.CharField(max_length=15, null=True),
        ),
    ]