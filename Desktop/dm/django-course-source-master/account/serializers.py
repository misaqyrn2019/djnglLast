from django.db.models import fields
from rest_framework import serializers
from account.models import (Province,City)

class OBJProvince(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['Id','Name']

class OBJCity(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['Id','Name','IdProvince']