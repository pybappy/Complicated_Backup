from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def product(request):
   return  HttpResponse("My Product Page")