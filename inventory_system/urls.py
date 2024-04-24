from django.urls import path
from .views import ResourceTypeView
from.views import DepartmentView
from.views import ResourcesView
from.views import VendorView
from.views import PurchaseView

# from.views import *

urlpatterns = [
    path('resource_type/',ResourceTypeView.as_view({'get':'list','post':'create'})),
    path('resource_type/<int:pk>/',ResourceTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('department/',DepartmentView.as_view({'get':'list','post':'create'})),
    path('department/<int:pk>/',DepartmentView.as_view({'get':'retrieve','delete':'destroy','put':'update'})),

    path('resources/',ResourcesView.as_view({'get':'list','post':'create'})),
    path('resources/<int:pk>/',ResourcesView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('vendor/',VendorView.as_view({'get':'list','post':'create'})),
    path('vendor/<int:pk>/',VendorView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('purchase/',PurchaseView.as_view({'get':'list','post':'create'})),
    path('purchase/<int:pk>/',PurchaseView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]

