# Generated by Django 3.2.5 on 2021-09-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0003_auto_20210928_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='AssignmentDate',
            field=models.DateTimeField(verbose_name='تاریخ واگذاری'),
        ),
    ]
