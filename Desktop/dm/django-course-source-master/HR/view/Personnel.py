from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey
from django.shortcuts import render,redirect
from django.urls import reverse
from django.urls import reverse_lazy
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
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from HR.serializers import *
from HR.models import *
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView,RetrieveAPIView

class ApiPersonnel(LoginRequiredMixin,ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = OBJPersonnel

class ApiPersonnelFilterGroup(LoginRequiredMixin,ListCreateAPIView):
    serializer_class = OBJPersonnel

    def get_queryset(self, **kwargs):
        IdGroup = self.kwargs.get('IdGroup')
        return  Personnel.objects.filter(IdGroup=IdGroup)

class APIPost(LoginRequiredMixin,ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = ObjPost

class APIGroup(LoginRequiredMixin,ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = ObjGroup

class APIFieldofStudy(LoginRequiredMixin,ListCreateAPIView):
    queryset = FieldofStudy.objects.all()
    serializer_class = ObjFieldofStudy
