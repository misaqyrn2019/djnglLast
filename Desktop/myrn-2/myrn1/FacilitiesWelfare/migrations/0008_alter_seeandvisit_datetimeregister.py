# Generated by Django 3.2.5 on 2021-09-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0007_auto_20210928_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeandvisit',
            name='DateTimeRegister',
            field=models.DateTimeField(verbose_name='زمان عیادت'),
        ),
    ]
