from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    name=request
    return render(request,"index.html",{'name':name})

def saveTodb(request,name):
    blog.objects.create(name=name)
    obj=blog.objects.all()
    number=obj.count()
    return render(request,"particu.html",{'name':name,'number':number})