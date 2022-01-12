from rest_framework import serializers
from .models import *
from drf_dynamic_fields import DynamicFieldsMixin

class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        exclude = '__all__'

class Storeroomserializer(serializers.ModelSerializer):
    class Meta:
        model = Storeroom
        fields = '__all__'

class UnitofMeasurementserializer(serializers.ModelSerializer):
    class Meta:
        model = UnitofMeasurement
        fields = '__all__'


class GroupCommodityserializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCommodity
        fields = '__all__'

class CategoryCommodityserializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryCommodity
        fields = '__all__'

class UnitPackserializer(serializers.ModelSerializer):
    class Meta:
        model = UnitPack
        fields = '__all__'

class Supplierserializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        
class Commodityserializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'