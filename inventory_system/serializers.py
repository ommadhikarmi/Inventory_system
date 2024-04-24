from rest_framework import serializers
from .models import * # '*'--all models Res

class ResourceTypeSerializer(serializers.ModelSerializer):
    class Meta: # define extra freatures
        model = ResourceType
        fields = '__all__' # name should be same

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'