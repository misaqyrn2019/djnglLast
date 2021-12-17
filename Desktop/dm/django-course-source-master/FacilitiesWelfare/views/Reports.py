from django.shortcuts import render
from FacilitiesWelfare.models.Projects import RegisterProject
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
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from FacilitiesWelfare.models.Assistance import *
from django.contrib.auth.mixins import LoginRequiredMixin

class Report(FacilitiesWelfareAccessMixin,ListView):
    template_name = "FacilitiesWelfare/Reports/Reports.html"
    model = Assistance
    lookup_field = "IdUser"

    def get_context_data(self, **kwargs):
        IdUser = self.kwargs.get('IdUser')
        DateStart = self.kwargs.get('DateStart')
        DateEnd = self.kwargs.get('DateEnd')
        
        context = super().get_context_data(**kwargs)
        context['Personnel'] = Personnel.objects.all()

        if IdUser == None or DateStart == None or DateEnd == None :
            return context
        
        context['FreeHelp'] = FreeHelp.objects.filter(Q(DateRegister__gte=DateStart) & Q(DateRegister__lte=DateEnd) & Q(IdUser=IdUser))
        context['Reward'] = Reward.objects.filter(Q(AssignmentDate__gte=DateStart) & Q(AssignmentDate__lte=DateEnd) & Q(IdUser=IdUser))
        context['SeeAndVisit'] = SeeAndVisit.objects.filter(Q(DateTimeVisit__gte=DateStart) & Q(DateTimeVisit__lte=DateEnd) & Q(IdUser=IdUser))
        context['Travels'] = Travels.objects.filter(Q(StartDateTime__gte=DateStart) & Q(EndDateTime__lte=DateEnd) & Q(IdUser=IdUser))
        context['RegisterLoan'] = RegisterLoan.objects.filter(Q(RegisterDateTime__gte=DateStart) & Q(RegisterDateTime__lte=DateEnd) & Q(IdUser=IdUser))
        context['RegisterAssistance'] = RegisterAssistance.objects.filter(Q(DateTimeRegister__gte=DateStart) & Q(DateTimeRegister__lte=DateEnd) & Q(IdUser=IdUser))
        context['CashAssistance'] = CashAssistance.objects.filter(Q(DateRegister__gte=DateStart) & Q(DateRegister__lte=DateEnd) & (Q(IdUser=IdUser) | Q(TypeAssistance="PU")))
        context['ConsumerItemsRegister'] = ConsumerItemsRegister.objects.filter(Q(DateRegister__gte=DateStart) & Q(DateRegister__lte=DateEnd) & Q(IdUser=IdUser))
        context['RegisterProject'] = RegisterProject.objects.filter(Q(RegisterDateTime__gte=DateStart) & Q(RegisterDateTime__lte=DateEnd) & Q(IdUser=IdUser))
        
        return context