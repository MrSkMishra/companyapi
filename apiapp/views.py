import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from apiapp.models import Company,Employee
from apiapp.serializers import CompanySerializer,EmployeeSerializer
import requests
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            print(f"method get employees of {pk} company")
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e :
            print(e)
            return Response({
                'message':"Company might not exist"
            })


def apikey(request):
    # response = requests.get('https://justforpay.in/production/testapi/dmt_reqeust').json()
    
    response = requests.get('https://api.covid19api.com/countries').json()
    res = {"Country":response,
            "Slug":response,
            "ISO2":response

    }
    
    return JsonResponse(res,content_type="application/json")

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
