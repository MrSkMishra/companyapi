from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

def home_page(request):
    print("Home Page Requested")
    friend = [
        'easy',
        'something',
        'nothing'
    ]
    return JsonResponse(friend,safe=False)


