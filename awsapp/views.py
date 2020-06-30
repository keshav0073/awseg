from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    return HttpResponse("You are on home page")