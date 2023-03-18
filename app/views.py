from django.shortcuts import render

from .models import *
from . import models

# def savdo(request):
# 	objs = Savdo.objects.all()
	
# 	return render(request , "total.html",{"objs":objs})


def all(request):
	 
    category_data=models.Magazinlar.objects.all()
    category_data1=models.Savdo.objects.all()
    return render(request,'magazin.html',{'data':category_data,'data1':category_data1})
def index(request,test_id):
    dukon=models.Magazinlar.objects.get(id=test_id)
    questions=models.Savdo.objects.filter(dukon=dukon)

   
    return render(request,'qarz.html',{'objs':questions,'dukon':dukon})

def xarajat(request):
	ok = Xarajat.objects.all()
	
	return render(request , "xarajatlar.html",{"ok":ok})
