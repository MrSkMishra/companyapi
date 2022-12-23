from django.urls import path,include
from apiapp.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)

urlpatterns = [
    
    path('',include(router.urls)),
    path('hello',views.apikey,name="api"),
]
