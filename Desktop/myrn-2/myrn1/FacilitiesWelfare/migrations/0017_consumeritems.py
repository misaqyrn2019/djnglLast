# Generated by Django 3.2.5 on 2021-09-29 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FacilitiesWelfare', '0016_alter_cashassistance_dateregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerItems',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('TypeAssistance', models.CharField(choices=[('F', 'رایگان'), ('C', 'نقدی')], default='F', max_length=1, verbose_name='نوع')),
                ('Items', models.CharField(max_length=500, verbose_name='اقلام')),
                ('DateRegister', models.DateTimeField(verbose_name='تاریخ ثبت')),
                ('DateExpire', models.DateTimeField(verbose_name='تاریخ انقضا')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('IdUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='شناسه کاربر')),
            ],
            options={
                'verbose_name': 'کمک معیشتی نقدی',
                'verbose_name_plural': 'کمک های معیشتی',
            },
        ),
    ]
