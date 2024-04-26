from django.shortcuts import render, get_object_or_404, redirect


from django.db import models
from .models import *
from django.contrib import *
from company.models import Jobdetails

# Create your views here.
#projecthomepage
def adminhomepage(request):
    return render(request,'adminhomepage.html')

def view_job_details(request):
    job_details_list = Jobdetails.objects.all()
    return render(request, 'ADViewJobdetails.html', {'job_details_list': job_details_list})

def delete_jobdetails(request, job_id):
    job_details = get_object_or_404(Jobdetails, id=job_id)
    job_details.delete()
    return redirect('Aview_job_details')

def application(request):
    return render(request,'ADViewJobdetails.html')

import re
from django.shortcuts import render
from django.contrib.auth.models import User

def usernames_non_numeric(request):
    non_numeric_usernames = User.objects.exclude(username__regex=r'^\d').exclude(username='admin').exclude(username='KLU')
    return render(request, 'companynames.html', {'usernames': non_numeric_usernames})


def usernames_with_numeric(request):
    numeric_usernames = User.objects.filter(username__regex=r'^\d')
    return render(request, 'studentnames.html', {'usernames': numeric_usernames})

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def delete_userSN(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        # Add any necessary validation or permission checks here
        user.delete()
        return redirect('AstudentNames')  # Redirect to a suitable URL after deletion
    else:
        # Handle GET request, if required
        pass


def delete_userCN(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        # Add any necessary validation or permission checks here
        user.delete()
        return redirect('AcompanyNames')  # Redirect to a suitable URL after deletion
    else:
        # Handle GET request, if required
        pass