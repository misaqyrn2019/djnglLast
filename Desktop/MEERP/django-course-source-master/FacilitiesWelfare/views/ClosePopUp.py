from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic.base import View
from FacilitiesWelfare.models.Projects import Project
from account.mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin,
    FacilitiesWelfareAccessMixin
)
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
    DetailView
)
from django.urls import reverse_lazy
from extensions.utils import jalali_converter
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.models.Assistance import Assistance
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ClosePopUp(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Project
    template_name = "FacilitiesWelfare/ClosePopUp/ClosePopUp.html"

    def get_queryset(self):
        return Project.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Project, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs