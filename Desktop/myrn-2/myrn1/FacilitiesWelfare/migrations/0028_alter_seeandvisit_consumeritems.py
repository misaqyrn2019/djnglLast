# Generated by Django 3.2.5 on 2021-09-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacilitiesWelfare', '0027_alter_seeandvisit_consumeritems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeandvisit',
            name='ConsumerItems',
            field=models.CharField(choices=[('F', 'پدر'), ('M', 'مادر'), ('P', 'پدربزرگ'), ('Q', 'مادربزرگ'), ('B', 'برادر'), ('S', 'خواهر'), ('D', 'دایی'), ('A', 'عمو'), ('K', 'خاله'), ('E', 'عمه')], max_length=2, verbose_name='نسبت'),
        ),
    ]
