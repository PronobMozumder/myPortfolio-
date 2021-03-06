# Generated by Django 3.0.6 on 2020-05-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myinfo',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='proCount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='selfDec',
            field=models.TextField(),
        ),
    ]
