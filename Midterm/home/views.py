from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages
from .forms import Taskforms

# Create your views here.
def home(request):
    return render(request, 'index.html' )



def todo(request):
     try:
         data = Task.objects.all()
         context = {'task':data}
     except Exception as e:
         context = {'project':"No Data Found"}
     return render(request, 'services.html', context )

def taskform(request):
    form = Taskforms()
    context = {'form':form}
    if request.method == 'POST':
        myData = Taskforms(request.POST)
        if myData.is_valid():
            myData.save()
            messages.success(request,"Project Added Successfully")
            return redirect('todo')
    return render(request,'taskform.html',context)


def taskdelete(request, id):
    datadelete = Task.objects.get(id = id)
    datadelete.delete()
    messages.error(request,"Project Deleted Successfully")

    return redirect('todo')


def taskupdate(request,id):
    myData1 = Task.objects.get(id=id)
    updateform = Taskforms(request.POST or None ,instance = myData1) 
    if updateform.is_valid():
            updateform.save()
            messages.success(request,"Task Edited Successfully")
            return redirect('todo')
    context = {'form' : updateform}
    return render(request,"taskupdate.html", context)