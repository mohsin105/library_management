from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view()
def project_test(request):
    return Response({'message': 'Hello library management project'})

