from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey
from django.urls.base import reverse_lazy
from rest_framework.views import APIView
from FacilitiesWelfare.models.Projects import TypeProject
from account.mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin,
    FacilitiesWelfareAccessMixin,
)
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
    DetailView
)
from account.models import City,Province
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from HR.serializers import *
from HR.models import *
from extensions.utils import jalali_converter
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView,RetrieveAPIView,UpdateAPIView
#*************************************************************************************************
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd
from HR.froms import *
from django.shortcuts import redirect
from datetime import datetime

class ApiLISTPersonnel(LoginRequiredMixin,ListAPIView):
    queryset = Personnel.objects.all().order_by('Id')
    serializer_class = OBJPersonnel

class ApiPersonnel(LoginRequiredMixin,CreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = OBJPersonnel

class ApiUpdatePersonnel(LoginRequiredMixin,UpdateAPIView):
    queryset = Personnel.objects.all()
    success_url = reverse_lazy('HR:ListPersonnel')
    serializer_class = OBJPersonnel

    def form_valid(self,form):
        form = form.save(commit=False)

        pk = self.request.POST.get('pk')
        print("****************************************************" + str(pk))
        form.save()

class UpdatePersonnel(LoginRequiredMixin,DefinePersonnel,UpdateView):
    model = Personnel
    success_url = reverse_lazy('HR:ListPersonnel')
    template_name = "HR/Personnel/UpdatePersonnel.html"

class ApiPersonnelFilterGroup(LoginRequiredMixin,ListCreateAPIView):
    serializer_class = OBJPersonnel

    def get_queryset(self, **kwargs):
        IdGroup = self.kwargs.get('IdGroup')
        return  Personnel.objects.filter(IdGroup=IdGroup)

class APIOrganization(LoginRequiredMixin,ListCreateAPIView):
    queryset = Organization.objects.all().order_by('Id')
    serializer_class = ObjOrganization

class APIPost(LoginRequiredMixin,ListCreateAPIView):
    queryset = Post.objects.all().order_by('Id')
    serializer_class = ObjPost

class APIGroup(LoginRequiredMixin,ListCreateAPIView):
    queryset = Group.objects.all().order_by('Id')
    serializer_class = ObjGroup

class APIFieldofStudy(LoginRequiredMixin,ListCreateAPIView):
    queryset = FieldofStudy.objects.all().order_by('Id')
    serializer_class = ObjFieldofStudy
 

class Upload(LoginRequiredMixin,DefinePersonnel,CreateView):
    model = Personnel
    success_url = reverse_lazy('HR:CreatePersonnel')
    template_name = "HR/Personnel/Upload.html"

    def post(self,request,*args,**kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('PathFile')
        PathFile = str(files[0].file.name)
        df = pd.read_excel(PathFile,header=1)

        for index,row in df.iterrows():            
            Gender = 'M'
            IsActive = 'Y'
            IdGradeofStudy = 'KAR'
            MaritalStatus = 'N'

            if(row.MaritalStatus == 'مجرد'):
                MaritalStatus = 'N'
            elif(row.MaritalStatus == 'متاهل'):
                MaritalStatus = 'Y'
            else:
                MaritalStatus = 'Y'

            if(row.Gender == 'مذکر'):
                Gender = 'M';
            elif(row.Gender == 'مونث'):
                Gender = 'F';
            else:
                Gender = 'M';
            
            if(row.IsActive == 'فعال'):
                IsActive = 'Y'
            elif(row.IsActive == 'غیرفعال'):
                IsActive = 'N'
            else:
                IsActive = 'N'            

            if(row.IdGradeofStudy == 'سیکل'):
                IdGradeofStudy = 'SI'
            elif(row.IdGradeofStudy == 'دیپلم'):
                IdGradeofStudy = 'DI'
            elif(row.IdGradeofStudy == 'کاردانی'):
                IdGradeofStudy = 'KA'
            elif(row.IdGradeofStudy == 'کارشناسی'):
                IdGradeofStudy = 'KAR'
            elif(row.IdGradeofStudy == 'کارشناسی ارشد'):
                IdGradeofStudy = 'ARS'
            elif(row.IdGradeofStudy == 'دکتری'):
                IdGradeofStudy = 'DR'
            elif(row.IdGradeofStudy == 'فوق دکتری'):
                IdGradeofStudy = 'FDR'
            elif(row.IdGradeofStudy == 'پزشک'):
                IdGradeofStudy = 'PE'
            elif(row.IdGradeofStudy == 'پزشک متخصص'):
                IdGradeofStudy = 'PEM'
            else:
                IdGradeofStudy = 'SI'

            CountOrganization = Organization.objects.filter(Title = row.IdOrganization).count()
            if(CountOrganization == 0):
                ORG = Organization.objects.create(Title=row.IdOrganization)
                ORG.save()
            IdOrganization = Organization.objects.filter(Title = row.IdOrganization)

            CountProItem = Province.objects.filter(Name = row.IdProvince).count()
            if(CountProItem == 0):
                PROV = Province.objects.create(Name=row.IdProvince)
                PROV.save()
            IdProvince = Province.objects.filter(Name = row.IdProvince)
            
            CountCityItem = City.objects.filter(Name = row.IdCity).count()
            if(CountCityItem == 0):
                CityCRT = City.objects.create(Name=row.IdCity,IdProvince_id=IdProvince[0].Id)
                CityCRT.save()
            IdCity = City.objects.filter(Name = row.IdCity)

            CountGroup = Group.objects.filter(Title = row.IdGroup).count()
            if(CountGroup == 0):
                GRP = Group.objects.create(Title=row.IdGroup)
                GRP.save()
            IdGroup = Group.objects.filter(Title = row.IdGroup)

            CountPost = Post.objects.filter(Title = row.IdPost).count()
            if(CountPost == 0):
                PST = Post.objects.create(Title=row.IdPost)
                PST.save()
            IdPost = Post.objects.filter(Title = row.IdPost)

            CountFieldofStudy = FieldofStudy.objects.filter(Title = row.IdFieldofStudy).count()
            if(CountFieldofStudy == 0):
                FOS = FieldofStudy.objects.create(Title=row.IdFieldofStudy)
                FOS.save()
            IdFieldofStudy = FieldofStudy.objects.filter(Title = row.IdFieldofStudy)

            try:
                Pl = Personnel.objects.create(
                    Name = row.Name,
                    Family = row.Family,
                    DateBirthDay = datetime.fromisoformat(str(row.DateBirthDay)),
                    Address = row.Address,
                    NationalCode = row.NationalCode,
                    IdNumber = row.IdNumber,
                    HomePhoneNumber = row.HomePhoneNumber,
                    MobileNumber = row.MobileNumber,
                    EmergencyNumber = row.EmergencyNumber,
                    Email = row.Email,
                    UserName = row.UserName,
                    Password = row.Password,
                    DateMarried = datetime.fromisoformat(str(row.DateMarried)),
                    Gender = Gender,
                    MaritalStatus = MaritalStatus,
                    IsActive = IsActive,
                    IdGradeofStudy = IdGradeofStudy,
                    IdProvince_id = IdProvince[0].Id,
                    IdCity_id = IdCity[0].Id,
                    IdFieldofStudy_id = IdFieldofStudy[0].Id,
                    IdPost_id = IdPost[0].Id,
                    IdGroup_id = IdGroup[0].Id,
                    IdOrganization_id = IdOrganization[0].Id
                )
                Pl.save()
            except:
                continue
        return redirect(reverse_lazy('HR:ListPersonnel'))

class CreatePersonnel(LoginRequiredMixin,DefinePersonnel,CreateView):
    model = Personnel
    success_url = reverse_lazy('HR:CreatePersonnel')
    template_name = "HR/Personnel/CreatePersonnel.html"

class ListPersonnel(LoginRequiredMixin,DefinePersonnel,ListView):
    model = Personnel
    template_name = "HR/Personnel/ListPersonnel.html"

    def get_queryset(self):
        return Personnel.objects.all().order_by('Id')

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)