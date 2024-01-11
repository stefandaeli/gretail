from django.shortcuts import render

def index(request):
    context ={
        'name' : 'stefan'
    }
    return render(request,'index.html',context)
