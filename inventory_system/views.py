from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from.models import ResourceType 
from.models import Department  # import table models which used in queryset
from.models import Resources
from.models import Vendor
from.models import Purchase
#from.models import *

from.serializers import ResourceTypeSerializer
from.serializers import DepartmentSerializer
from.serializers import ResourcesSerializer
from.serializers import VendorSerializer
from.serializers import PurchaseSerializer

# from.serializers import *

# Create your views here.
class ResourceTypeView(ModelViewSet):
    queryset = ResourceType.objects.all()  # we have to define which table should operate CRUD operation.
    serializer_class = ResourceTypeSerializer

class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ResourcesView(ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer

class VendorView(ModelViewSet):
    queryset =Vendor.object.all()
    serializer_class = VendorSerializer

class PurchaseView(ModelViewSet):
    queryset = Purchase.object.all()
    serializer_class =PurchaseSerializer
    

