# Generated by Django 2.0.3 on 2018-04-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20180423_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='creat_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
    ]
