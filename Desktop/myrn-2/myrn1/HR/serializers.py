from django.db.models import fields
from rest_framework import serializers
from account.models import (Province,City)
from HR.models import *

class OBJPersonnel(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['Id','Name','Family','DateBirthDay','Address','NationalCode','IdNumber','HomePhoneNumber','MobileNumber','EmergencyNumber','Email','UserName','Password','DateMarried','Gender','MaritalStatus','IsActive','IdProvince','IdGradeofStudy','IdCity','IdFieldofStudy','IdPost','IdGroup','IdOrganization']

class ObjFieldofStudy(serializers.ModelSerializer):
    class Meta:
        model = FieldofStudy
        fields = ['Id','Title']

class ObjPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['Id','Title']

class ObjGroup(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['Id','Title']

class ObjOrganization(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'