from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    name=request
    return render(request,"index.html",{'name':name})