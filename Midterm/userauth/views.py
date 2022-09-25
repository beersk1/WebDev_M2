from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

# Create your views here.




def signuppage(request):
    if request.method=="POST":
        data=SignupForm(request.POST)
        if data.is_valid():
            new_user=data.save()

            login(request, new_user)
            return redirect('home')
    else:
        data=SignupForm()

    return render(request, "signup.html", {"form":data})








def loginpage(request):
    if request.method =='POST':
        name = request.POST['username']
        password = request.POST['password']
        print(name, password)
        user = authenticate(request, username = name, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Credentials not found!!")


    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('home')



