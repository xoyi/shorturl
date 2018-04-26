# Generated by Django 2.0.3 on 2018-04-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20180423_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroinfo',
            old_name='sex',
            new_name='is_deleted',
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='creat_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
