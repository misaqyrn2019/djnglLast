# Generated by Django 3.2.5 on 2021-09-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0006_alter_registerorganizationalhouse_dateexpire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationalhouse',
            name='DateExpire',
            field=models.DateTimeField(verbose_name='تاریخ انقضا'),
        ),
        migrations.AlterField(
            model_name='organizationalhouse',
            name='DateRegister',
            field=models.DateTimeField(verbose_name='تاریخ ثبت'),
        ),
    ]
