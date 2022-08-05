from tkinter import CHAR
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import person

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if person.objects.filter(username=username,password=password).exists():
            obj = person.objects.get(username=username,password=password)
            return render(request,'index.html',{'obj':obj})
        else:
            messages.info('Invalid credentials!')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        address = request.POST['address']
        f=request.POST['fname']
        l=request.POST['lname']
        
        if password1 == password2:
            if person.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif person.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                user = person.objects.create(firstname=f,lastname=l,username=username, email=email, password=password1,address=address)
                return redirect('login')
        else:
            messages.info(request,'Wrong passwords')
            return redirect('register')
    else:
        return render(request,'register.html')
