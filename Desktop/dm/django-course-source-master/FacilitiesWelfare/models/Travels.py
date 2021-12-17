from django.db import models
from django.utils import timezone
from HR.models.Personnel import Personnel
from account.models import Province,City
from django.db.models import Q, Sum, Count
from extensions.utils import jalali_converter,jalali_converterWT
from django.contrib.auth import get_user_model

class Travels(models.Model):
    STATUS = (
		('s', 'سیاحتی'),
		('z', "زیارتی"),
        ('m', "ماموریت کاری")
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه")
    IdCity = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name= "شهر")
    StartDateTime = models.DateTimeField(verbose_name="تاریخ شروع")
    EndDateTime = models.DateTimeField(verbose_name="تاریخ پایان")
    Description = models.TextField(verbose_name="توضیحات",null=True,blank=True)
    status = models.CharField(max_length=1, choices=STATUS, verbose_name="نوع سفر",default="s")
    IdUser = models.ForeignKey(Personnel, on_delete=models.CASCADE,verbose_name= "پرسنل")

    class Meta:
        verbose_name = "سفر"
        verbose_name_plural = "سفرها"

    def __str__(self):
        return str(self.Id)

    def jStartDateTime(self):
        return jalali_converterWT(self.StartDateTime)
    jStartDateTime.short_description = "تاریخ شروع"
    
    def jEndDateTime(self):
        return jalali_converterWT(self.EndDateTime)
    jEndDateTime.short_description = "تاریخ پایان"

    def MStartDateTime(self):
        return str(self.StartDateTime.year) + "-" + str(self.StartDateTime.month) + "-" + str(self.StartDateTime.day)
    
    def MEndDateTime(self):
        return str(self.EndDateTime.year) + "-" + str(self.EndDateTime.month) + "-" + str(self.EndDateTime.day)