# Generated by Django 3.2.5 on 2021-10-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0031_consumeritems_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumeritemsregister',
            name='IsReceived',
            field=models.CharField(choices=[('Y', 'تحویل شده'), ('N', 'تحویل نشده')], default='N', max_length=1, verbose_name='تحویل شده'),
        ),
    ]
