from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from HR.models.Personnel import Personnel
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT

class Assistance(models.Model):#8-9-10
    Type = (
        ('CA', "کمک معیشتی"),
        ('CI', "اقلام مصرفی"),
        ('FH', "کمک بلاعوض"),
    )
    TypeAssistance = (
        ('PU', "همگانی"),
        ('PR', "خاص"),
        ('N', "بدون انتخاب"),
    )
    TypeItems = (
        ('Fr', "رایگان"),
        ('Ca', "نقدی"),
        ('N', "بدون انتخاب"),
    )
    TypeHelp = (
        ('Ma', "ازدواج"),
        ('BG', "هدیه تولد"),
        ('NC', "فرزند جدید"),
        ('N', "بدون انتخاب"),
    )
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    ConsumerType = models.CharField(max_length=2, choices=Type, verbose_name="نوع")
    TypeAssistance = models.CharField(max_length=2, choices=TypeAssistance, default="N", verbose_name="نوع کمک")
    ConsumerTypeItems = models.CharField(max_length=2, choices=TypeItems, default="N",verbose_name="آیتم")
    FreeHelp = models.CharField(max_length=2, choices=TypeHelp, default="N", verbose_name="نوع هدیه")
    Title = models.CharField(max_length=200, verbose_name="عنوان")
    Description = models.TextField(verbose_name="توضیحات",null=True,blank=True)
    DateRegister = models.DateTimeField(verbose_name="تاریخ ثبت")
    DateExpire = models.DateTimeField(verbose_name="تاریخ انقضا")

    def jDateRegister(self):
        return jalali_converterWT(self.DateRegister)
    jDateRegister.short_description = "تاریخ ثبت"

    def MDateRegister(self):
        return str(self.DateRegister.year) + "-" + str(self.DateRegister.month) + "-" + str(self.DateRegister.day)

    def jDateExpire(self):
        return jalali_converterWT(self.DateExpire)
    jDateExpire.short_description = "تاریخ انقضا"

    def MDateExpire(self):
        return str(self.DateExpire.year) + "-" + str(self.DateExpire.month) + "-" + str(self.DateExpire.day)

    def __str__(self):
        self.Title

    class Meta:
        verbose_name = 'کمک'
        verbose_name_plural = 'کمک ها'

class RegisterAssistance(models.Model):
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    IdUser = models.ForeignKey(Personnel,on_delete=models.CASCADE,verbose_name="پرسنل")
    IdAssistance = models.ForeignKey(Assistance,on_delete=models.CASCADE,verbose_name="شناسه کمک")
    DateTimeRegister = models.DateTimeField(auto_now=True,verbose_name="زمان ثبت")

    def jDateTimeRegister(self):
        return jalali_converterWT(self.DateTimeRegister)

    def __str__(self):
        pass

    class Meta:
        verbose_name = "ثبت نام کمک"
        verbose_name_plural = "ثبت نام کمک ها"