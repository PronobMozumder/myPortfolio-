# Generated by Django 3.0.6 on 2020-05-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0009_auto_20200523_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='awardsInsName',
            field=models.CharField(default='a', max_length=600),
        ),
    ]
