from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'index.html')
def first(request):
    return render(request,'loginpage.html')
def role(request):
    return render(request,'roleselectionpage.html')

def studentsignup(request):
    return render(request,'studentsignup.html')

def companysignup(request):
    return render(request,'companysignup.html')

#register module Comapany
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest

def companyregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')
        # Validate username format
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                return HttpResponseBadRequest('Username already exists')
            else:
                user = User.objects.create_user(username=username, password=pass1, first_name=name, email=email)
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('first')
        else:
            return HttpResponseBadRequest('Passwords do not match')
    else:
        return HttpResponseBadRequest('Error')

#register module Student
def studentregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')
        # Validate username format
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                return HttpResponseBadRequest('Username already exists')
            elif len(username) != 10:
                return HttpResponseBadRequest('ID INVALID')
            else:
                user = User.objects.create_user(username=username, password=pass1, first_name=name, email=email)
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('first')
        else:
            return HttpResponseBadRequest('Passwords do not match')
    else:
        return HttpResponseBadRequest('Error')

















#logins logic
def logins(request):
    if request.method =='POST':
        username = request.POST['username']
        pass1=request.POST['password']
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username) == 10 and username.isdigit():
                return redirect('studenthomepage')
            elif username=="KLU":
                return redirect('adminhomepage')
            else:
                return redirect('companyhomepage')
        else:
            return HttpResponseBadRequest('INVALID U&P')

#logout
def logout(request):
    auth.logout(request)
    return render(request,'loginpage.html')