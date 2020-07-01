from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    name=request
    return render(request,"index.html",{'name':name})

def saveTodb(request,name):
    blog.objects.create(name=name)
    obj=blog.objects.all()
    print(obj.count())
    return HttpResponse(str(name)+"/n:saved in db:"+str(obj.count()))