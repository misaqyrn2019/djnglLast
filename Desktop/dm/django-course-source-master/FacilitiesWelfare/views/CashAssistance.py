from django.shortcuts import render
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
from django.urls import reverse_lazy,reverse
from extensions.utils import jalali_converter
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from django.shortcuts import render,redirect

class CashAssistanceList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = CashAssistance
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance_list.html"

    def get_queryset(self):
        return CashAssistance.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(CashAssistance, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class CashAssistanceCreate(FacilitiesWelfareAccessMixin,DefineCachAssistance,CreateView):
    model = CashAssistance
    success_url = reverse_lazy('FacilitiesWelfare:homeCA')
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance-create-update.html"

    def form_valid(self,form):
        form = form.save(commit=False)

        Personnels = self.request.POST.get('Personnels')
        CHKTF = self.request.POST.get('CHKTF')
        CHKGRP = self.request.POST.get('CHKGRP')
        IdGroup = self.request.POST.get('IdGroup')

        if str(CHKTF) == 'on' and str(CHKGRP) == 'on':
            p = Personnel.objects.filter(IdGroup = int(IdGroup))
            for item in p:
                Id = CashAssistance.objects.aggregate(Max('Id'))['Id__max']
                if str(Id) == 'None':
                    Id = '0'
                form.Id = (int(str(Id))) + 1
                form.IdUser = item
                form.save(force_insert=True, force_update=False)
        elif str(CHKTF) == 'on' and str(CHKGRP) == 'None':
            for item in Personnels.split(','):
                p = Personnel.objects.filter(Id = int(item))
                Id = CashAssistance.objects.aggregate(Max('Id'))['Id__max']
                if str(Id) == 'None':
                    Id = '0'
                form.Id = (int(str(Id))) + 1
                form.IdUser = p[0]
                form.save(force_insert=True, force_update=False)
        else:
            form.save()
        
        return redirect(reverse('FacilitiesWelfare:homeCA'))

class CashAssistanceUpdate(FacilitiesWelfareAccessMixin,DefineCachAssistance,UpdateView):
    model = CashAssistance
    success_url = reverse_lazy('FacilitiesWelfare:homeCA')
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance-create-update.html"

class CashAssistanceDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = CashAssistance
    success_url = reverse_lazy('FacilitiesWelfare:homeCA')
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance_confirm_delete.html"

class UserCashAssistance(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = CashAssistance
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance_list_User.html"

    def get_queryset(self):
        return CashAssistance.objects.filter(Q(IdUser=self.request.user) | Q(TypeAssistance="PU")).order_by("TypeAssistance")

    def get_object(self):
        return CashAssistance.objects.get(pk = self.request.user.pk)