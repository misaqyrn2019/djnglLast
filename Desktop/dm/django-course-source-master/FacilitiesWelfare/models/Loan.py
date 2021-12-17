from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from HR.models.Personnel import Personnel
from extensions.utils import jalali_converter,jalali_converterWT
import humanize

class Loan(models.Model):
    STATUS = (
		('S', 'وام کوتاه مدت'),#Short-Term Loan
		('L', "وام بلند مدت"),#Long-Term Loan
        ('m', "مساعده مالی")#Advanced Money
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه")
    StartDateTime = models.DateTimeField(verbose_name="تاریخ شروع")
    EndDateTime = models.DateTimeField(verbose_name="تاریخ پایان")
    TotalAmount = models.IntegerField(verbose_name="مبلغ کل")
    NumberInstallment = models.IntegerField(verbose_name="تعداد اقساط")
    InstallmentAmount = models.IntegerField(verbose_name="مبلغ قسط")
    LoanInterest = models.IntegerField(verbose_name="سود وام")
    Description = models.TextField(verbose_name="توضیحات",null=True,blank=True)
    status = models.CharField(max_length=1, choices=STATUS, verbose_name="نوع وام",default="s")
    Title = models.CharField(max_length=100, verbose_name="عنوان وام")

    def HInstallmentAmount(self):
        return humanize.intcomma(self.InstallmentAmount)
    HInstallmentAmount.short_description = "مبلغ قسط"

    def HTotalAmount(self):
        return humanize.intcomma(self.TotalAmount)
    HTotalAmount.short_description = "مبلغ کل"

    def jStartDateTime(self):
        return jalali_converterWT(self.StartDateTime)
    jStartDateTime.short_description = "تاریخ شروع"

    def MStartDateTime(self):
        return str(self.StartDateTime.year) + "-" + str(self.StartDateTime.month) + "-" + str(self.StartDateTime.day)

    def jEndDateTime(self):
        return jalali_converterWT(self.EndDateTime)
    jEndDateTime.short_description = "تاریخ پایان"

    def HEndDateTime(self):
        return humanize.naturaltime(self.EndDateTime)

    def MEndDateTime(self):
        return str(self.EndDateTime.year) + "-" + str(self.EndDateTime.month) + "-" + str(self.EndDateTime.day)

    class Meta:
        verbose_name = "وام"
        verbose_name_plural = "وام ها"

    def __str__(self):
        return str(self.Id) + "_" + self.Title

class RegisterLoan(models.Model):
    STATUSConfirmation = (
		('N', 'تایید نشده'),
		('Y', "تایید شده"),
	)
    STATUSLattery = (
		('N', 'برنده نشده'),
		('Y', "برنده شده"),
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه")
    IdLoan = models.ForeignKey(Loan,on_delete=models.CASCADE,verbose_name= "وام")
    IdUser = models.ForeignKey(Personnel, on_delete=models.CASCADE,verbose_name= "پرسنل")
    RegisterDateTime = models.DateTimeField(auto_now=True,verbose_name="زمان ثبت درخواست")
    statusConfirmation = models.CharField(max_length=1, choices=STATUSConfirmation, verbose_name="تاییدیه",default="N")
    statusLattery = models.CharField(max_length=1, choices=STATUSLattery, verbose_name="قرعه کشی",default="N")

    def jRegisterDateTime(self):
        return jalali_converterWT(self.RegisterDateTime)
    jRegisterDateTime.short_description = "زمان ثبت درخواست"

    class Meta:
        verbose_name = "درخواست وام"
        verbose_name_plural = "درخواست های وام"