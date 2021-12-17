from django.shortcuts import render,redirect
from django.urls import reverse
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
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max

class RewardList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = Reward
    template_name = "FacilitiesWelfare/Reward/Reward_list.html"

    def get_queryset(self):
        return Reward.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Reward, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class RewardCreate(FacilitiesWelfareAccessMixin,DefineReward,CreateView):
    model = Reward
    success_url = reverse_lazy('FacilitiesWelfare:homeFwR')
    template_name = "FacilitiesWelfare/Reward/Reward-create-update.html"

    def form_valid(self,form):
        form = form.save(commit=False)

        Personnels = self.request.POST.get('Personnels')
        CHKTF = self.request.POST.get('CHKTF')
        CHKGRP = self.request.POST.get('CHKGRP')
        IdGroup = self.request.POST.get('IdGroup')

        if str(CHKTF) == 'on' and str(CHKGRP) == 'on':
            p = Personnel.objects.filter(IdGroup = int(IdGroup))
            for item in p:
                Id = Reward.objects.aggregate(Max('Id'))['Id__max']
                if str(Id) == 'None':
                    Id = '0'
                form.Id = (int(str(Id))) + 1
                form.IdUser = item
                form.save(force_insert=True, force_update=False)
        elif str(CHKTF) == 'on' and str(CHKGRP) == 'None':
            for item in Personnels.split(','):
                p = Personnel.objects.filter(Id = int(item))
                Id = Reward.objects.aggregate(Max('Id'))['Id__max']
                if str(Id) == 'None':
                    Id = '0'
                form.Id = (int(str(Id))) + 1
                form.IdUser = p[0]
                form.save(force_insert=True, force_update=False)
        else:
            form.save()

        return redirect(reverse('FacilitiesWelfare:homeFwR'))

class RewardUpdate(FacilitiesWelfareAccessMixin,DefineReward,UpdateView):
    model = Reward
    success_url = reverse_lazy('FacilitiesWelfare:homeFwR')
    template_name = "FacilitiesWelfare/Reward/Reward-create-update.html"

class RewardDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = Reward
    success_url = reverse_lazy('FacilitiesWelfare:homeFwR')
    template_name = "FacilitiesWelfare/Reward/Reward_confirm_delete.html"

class UserReward(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Reward
    template_name = "FacilitiesWelfare/Reward/Reward_list_User.html"

    def get_queryset(self):
        return Reward.objects.filter(IdUser=self.request.user)