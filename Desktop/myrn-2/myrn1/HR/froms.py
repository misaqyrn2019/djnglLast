from django import forms
from django.db.models.base import Model
from django.forms import fields, models
from HR.models import *

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class DefinePersonnel(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = "__all__"