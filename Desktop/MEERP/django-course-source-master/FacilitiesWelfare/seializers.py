from django.db.models import fields
from rest_framework import serializers
from FacilitiesWelfare.models import *
from FacilitiesWelfare.models.Projects import TypeProject

class OBJTypeProject(serializers.ModelSerializer):
    class Meta:
        model = TypeProject
        fields = ['Id','Name']