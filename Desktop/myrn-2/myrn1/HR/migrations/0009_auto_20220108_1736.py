# Generated by Django 3.2.5 on 2022-01-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0008_auto_20220107_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='NumberPersonnel',
        ),
        migrations.AlterField(
            model_name='personnel',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شماره پرسنلی'),
        ),
    ]
