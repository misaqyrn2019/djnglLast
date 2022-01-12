# Generated by Django 3.2.5 on 2021-09-27 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0017_auto_20210830_2200'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('TypeAssistance', models.CharField(choices=[('PU', 'همگانی'), ('PR', 'خاص'), ('N', 'بدون انتخاب')], default='N', max_length=2, verbose_name='نوع کمک')),
                ('ConsumerItems', models.CharField(choices=[('Fr', 'رایگان'), ('Ca', 'نقدی'), ('N', 'بدون انتخاب')], default='N', max_length=2, verbose_name='آیتم')),
                ('FreeHelp', models.CharField(choices=[('Ma', 'ازدواج'), ('BG', 'هدیه تولد'), ('NC', 'فرزند جدید'), ('N', 'بدون انتخاب')], default='N', max_length=2, verbose_name='نوع هدیه')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('DateRegister', models.DateField(verbose_name='تاریخ ثبت')),
                ('DateExpire', models.DateField(verbose_name='تاریخ انقضا')),
            ],
            options={
                'verbose_name': 'کمک',
                'verbose_name_plural': 'کمک ها',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('StartDateTime', models.DateTimeField(verbose_name='تاریخ شروع')),
                ('EndDateTime', models.DateTimeField(verbose_name='تاریخ پایان')),
                ('TotalAmount', models.IntegerField(verbose_name='مبلغ کل')),
                ('NumberInstallment', models.IntegerField(verbose_name='تعداد اقساط')),
                ('InstallmentAmount', models.IntegerField(verbose_name='مبلغ قسط')),
                ('LoanInterest', models.IntegerField(verbose_name='سود وام')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('status', models.CharField(choices=[('S', 'وام کوتاه مدت'), ('L', 'وام بلند مدت'), ('m', 'مساعده مالی')], default='s', max_length=1, verbose_name='نوع وام')),
                ('Title', models.CharField(max_length=100, verbose_name='عنوان وام')),
            ],
            options={
                'verbose_name': 'وام',
                'verbose_name_plural': 'وام ها',
            },
        ),
        migrations.CreateModel(
            name='OrganizationalHouse',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('DateRegister', models.DateField(verbose_name='تاریخ ثبت')),
                ('DateExpire', models.DateField(verbose_name='تاریخ انقضا')),
                ('Description', models.TextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'خانه سازمانی',
                'verbose_name_plural': 'خانه های سازمانی',
            },
        ),
        migrations.CreateModel(
            name='TypeProject',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه نوع')),
                ('Name', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'نوع پروژه',
                'verbose_name_plural': 'انواع پروژه',
            },
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('StartDateTime', models.DateField(verbose_name='تاریخ شروع')),
                ('EndDateTime', models.DateField(verbose_name='تاریخ پایان')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('status', models.CharField(choices=[('s', 'سیاحتی'), ('z', 'زیارتی'), ('m', 'ماموریت کاری')], default='s', max_length=1, verbose_name='نوع سفر')),
                ('IdCity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.city', verbose_name='شهر')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفر',
                'verbose_name_plural': 'سفرها',
            },
        ),
        migrations.CreateModel(
            name='SeeAndVisit',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('ConsumerItems', models.CharField(choices=[('F', 'پدر'), ('M', 'مادر'), ('B', 'برادر'), ('S', 'خواهر')], max_length=2, verbose_name='نسبت')),
                ('Name', models.CharField(max_length=100, verbose_name='نام بیمار')),
                ('Family', models.CharField(max_length=100, verbose_name='نام خانوادگی بیمار')),
                ('DateTimeRegister', models.DateTimeField(auto_now=True, verbose_name='زمان ثبت')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='شناسه کاربر')),
            ],
            options={
                'verbose_name': 'دیدن و عیادت از بیمار',
                'verbose_name_plural': 'دید و عیادات از بیماران',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان پاداش')),
                ('AssignmentDate', models.DateField(verbose_name='تاریخ واگذاری')),
                ('Price', models.IntegerField(verbose_name='مبلغ پاداش')),
                ('Description', models.CharField(max_length=200, verbose_name='توضیحات')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پاداش',
                'verbose_name_plural': 'پاداش ها',
            },
        ),
        migrations.CreateModel(
            name='RelativesDeathServices',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('Name', models.CharField(max_length=50, verbose_name='نام')),
                ('Family', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('DeathDate', models.DateTimeField(verbose_name='تاریخ فوت')),
                ('Relation', models.CharField(choices=[('FA', 'پدر'), ('MO', 'مادر'), ('Lo', 'همسر'), ('GF', 'پدربزرگ'), ('GM', 'مادربزرگ'), ('UF', 'عمو'), ('UM', 'دایی'), ('AF', 'عمه'), ('AM', 'خاله')], max_length=2, verbose_name='نسبت')),
                ('Description', models.CharField(max_length=200, verbose_name='توضیحات')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'خدمات فوت بستگان',
                'verbose_name_plural': 'خدمات فوت بستگان',
            },
        ),
        migrations.CreateModel(
            name='RegisterOrganizationalHouse',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('DateTimeRegister', models.DateTimeField(auto_now=True, verbose_name='زمان ثبت')),
                ('DateExpire', models.DateField(verbose_name='تاریخ انقضا')),
                ('IdOrganizationHouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacilitiesWelfare.organizationalhouse', verbose_name='شناسه خانه')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='شناسه کاربر')),
            ],
            options={
                'verbose_name': 'ثبت نام خانه سازمانی',
                'verbose_name_plural': 'ثبت نام خانه های سازمانی',
            },
        ),
        migrations.CreateModel(
            name='RegisterLoan',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('RegisterDateTime', models.DateTimeField(auto_now=True, verbose_name='زمان ثبت درخواست')),
                ('statusConfirmation', models.CharField(choices=[('N', 'تایید نشده'), ('Y', 'تایید شده')], default='N', max_length=1, verbose_name='تاییدیه')),
                ('statusLattery', models.CharField(choices=[('N', 'برنده نشده'), ('Y', 'برنده شده')], default='N', max_length=1, verbose_name='قرعه کشی')),
                ('IdLoan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacilitiesWelfare.loan', verbose_name='وام')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'درخواست وام',
                'verbose_name_plural': 'درخواست های وام',
            },
        ),
        migrations.CreateModel(
            name='RegisterAssistance',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('DateTimeRegister', models.DateTimeField(auto_now=True, verbose_name='زمان ثبت')),
                ('IdAssistance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacilitiesWelfare.assistance', verbose_name='شناسه کمک')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='شناسه کاربر')),
            ],
            options={
                'verbose_name': 'ثبت نام کمک',
                'verbose_name_plural': 'ثبت نام کمک ها',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='شناسه')),
                ('Name', models.CharField(max_length=200, verbose_name='عنوان پروژه')),
                ('RegisterDateTime', models.DateTimeField(auto_now=True)),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('Address', models.CharField(max_length=200, verbose_name='آدرس')),
                ('IdCity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.city', verbose_name='شهر')),
                ('IdTypeProject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacilitiesWelfare.typeproject', verbose_name='نوع پروژه')),
                ('IdUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه ها',
            },
        ),
    ]
