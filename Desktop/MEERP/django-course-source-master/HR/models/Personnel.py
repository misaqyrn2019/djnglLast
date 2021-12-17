from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField
from django.utils import timezone
from django.contrib.auth.models import User
from account.models import City,Province
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT

class FieldofStudy(models.Model):
    Id = models.AutoField(unique=True,primary_key=True)
    Title = models.CharField(max_length=100,verbose_name="عنوان")#عنوان

    class Meta:
        verbose_name = "رشته تحصیلی"
        verbose_name_plural = "رشته تحصیلی"
    
    def __str__(self):
        return self.Title

class Post(models.Model):
    Id = models.AutoField(unique=True,primary_key=True)
    Title = models.CharField(max_length=100,verbose_name="عنوان")#عنوان

    class Meta:
        verbose_name = "سمت"
        verbose_name_plural = "سمت"
    
    def __str__(self):
        return self.Title

class Group(models.Model):
    Id = models.AutoField(unique=True,primary_key=True)
    Title = models.CharField(max_length=100,verbose_name="عنوان")#عنوان

    class Meta:
        verbose_name = "گروه"
        verbose_name_plural = "گروه"
    
    def __str__(self):
        return self.Title

class Personnel(models.Model):
    Sex = (('M','مذکر'),('F','مونث'))
    MS = (('N','مجرد'),('Y','متاهل'))
    Active = (('Y','فعال'),('N','غیرفعال'))
    GradeofStudy = (
        ('SI','سیکل'),
        ('DI','دیپلم'),
        ('KA','کاردانی'),
        ('KAR','کارشناسی'),
        ('ARS','کارشناسی ارشد'),
        ('DR','دکتری'),
        ('FDR','فوق دکتری'),
        ('PE','پزشک'),
        ('PEM','پزشک متخصص'),
    )

    Id = models.AutoField(unique=True,primary_key=True)
    NumberPersonnel = models.IntegerField(unique=True,verbose_name="شماره پرسنلی")#شماره پرسنلی
    Name = models.CharField(max_length=100,verbose_name="نام")#نام
    Family = models.CharField(max_length=100,verbose_name="نام خانوادگی")#نام خانوادگی
    DateBirthDay = models.DateField(verbose_name="تاریخ تولد")#تاریخ تولد
    Address = models.TextField(verbose_name="آدرس")#آدرس
    NationalCode = models.CharField(max_length=10,verbose_name="کد ملی")#کدملی
    IdNumber = models.CharField(max_length=10,verbose_name="شماره شناسنامه")#شماره شناسنامه
    HomePhoneNumber = models.CharField(max_length=10,verbose_name="شماره منزل")#شماره تماس منزل
    MobileNumber = models.CharField(max_length=10,verbose_name="شماره همراه")#شماره همراه
    EmergencyNumber = models.CharField(max_length=10,verbose_name="شماره اضطراری")#شماره اضطراری
    Email = models.EmailField(max_length=50,verbose_name="ایمیل")#ایمیل
    UserName = models.CharField(max_length=50,verbose_name="نام کاربری")#نام کاربری
    Password = models.CharField(max_length=50,verbose_name="رمز عبور")#رمز عبور
    DateMarried = models.DateField(verbose_name="تاریخ ازدواج")#تاریخ ازدواج
    RegisterDateTime = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")#تاریخ ثبت
    Gender = models.CharField(choices=Sex,max_length=1,default="M",verbose_name="جنسیت")#جنسیت
    MaritalStatus = models.CharField(choices=MS,max_length=1,default="Y",verbose_name="وضعیت تاهل")#وضعیت تاهل
    IsActive = models.CharField(choices=Active,max_length=1,default="Y",verbose_name="فعال")#فعال
    IdProvince = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name="نام استان")#شناسه استان محل تولد
    IdGradeofStudy = models.CharField(choices=GradeofStudy,default="KAR",max_length=3,verbose_name="مقطع تحصیلی")#مقطع تحصیلی
    IdCity = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="نام شهرستان")#شناسه شهرستان محل تولد
    IdFieldofStudy = models.ForeignKey(FieldofStudy,on_delete=models.CASCADE,verbose_name="رشته تحصیلی")#رشته تحصیلی
    IdPost = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="سمت")#سمت
    IdGroup = models.ForeignKey(Group,on_delete=models.CASCADE,verbose_name="گروه")#گروه

    class Meta:
        verbose_name = "پرسنل"
        verbose_name_plural = "پرسنل ها"
    
    def __str__(self):
        return str(self.Id) + "_" + self.Name + " " + self.Family

class ProfileofChildren(models.Model):
    Sex = (('M','مذکر'),('F','مونث'))
    
    Id = models.AutoField(unique=True,primary_key=True)
    Name = models.CharField(max_length=100,verbose_name="نام")#نام
    Family = models.CharField(max_length=100,verbose_name="نام خانوادگی")#نام خانوادگی
    Gender = models.CharField(choices=Sex,max_length=1,default="M",verbose_name="جنسیت")#جنسیت
    NationalCode = models.CharField(max_length=10,verbose_name="کد ملی")#کدملی
    BirthDate = models.DateField(verbose_name="تاریخ تولد")#تاریخ تولد
    IdPersonnel = models.ForeignKey(Personnel,on_delete=models.CASCADE,verbose_name="پرسنل")#پرسنل

    class Meta:
        verbose_name = "فرزند"
        verbose_name_plural = "فرزندان"
    
    def __str__(self):
        return str(self.Id) + "_" + self.Name + " " + self.Family