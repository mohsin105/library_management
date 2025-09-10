from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def home_page(request):
    return Response({'message':'This is the home page of Library Management'})