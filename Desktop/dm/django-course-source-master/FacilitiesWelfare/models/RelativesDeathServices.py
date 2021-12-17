from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from account.models import Province,City
from extensions.utils import jalali_converter,jalali_converterWT
from HR.models import *

class RelativesDeathServices(models.Model):
    STATUS_CHOICES = (
        ('FA', 'پدر'),
        ('MO', "مادر"),
        ('Lo', "همسر"),
        ('GF', "پدربزرگ"),
        ('GM', "مادربزرگ"),
        ('UF', "عمو"),#Uncle Father
        ('UM', "دایی"),#Uncle Mother
        ('AF', "عمه"),#Aunt Father
        ('AM', "خاله"),#Aunt Mother

    )

    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه")
    Name =models.CharField(max_length=50, verbose_name="نام")
    Family = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    DeathDate = models.DateTimeField(verbose_name="تاریخ فوت")
    IdUser = models.ForeignKey(Personnel, on_delete=models.CASCADE,verbose_name= "پرسنل")
    Relation = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name="نسبت")
    Description = models.CharField(max_length=200,verbose_name="توضیحات",null=True,blank=True)

    def jDeathDate(self):
        return jalali_converterWT(self.DeathDate)
    jDeathDate.short_description = "تاریخ ثبت"

    def MDeathDate(self):
        return str(self.DeathDate.year) + "-" + str(self.DeathDate.month) + "-" + str(self.DeathDate.day)

    def __str__(self):
        self.Name + " " + self.Family

    class Meta:
        verbose_name = 'خدمات فوت بستگان'
        verbose_name_plural = 'خدمات فوت بستگان'