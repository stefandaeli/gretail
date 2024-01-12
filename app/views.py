from django.shortcuts import render
from .models import *

def index(request):
    context ={
        'name' : 'stefan'
    }
    return render(request,'index.html',context)

def v_owners(request):
    data_owners = Owners.objects.all().order_by('owner_id')
    context = {
        'data_owners' : data_owners
    }
    return render (request,'owners/v_owners.html',context)