from django.shortcuts import render, get_object_or_404

from django.db import models
from .models import *
from django.contrib import *

from company.models import Jobdetails

# Create your views here.
def studenthomepage(request):
    return render(request,'studenthomepage.html')

def applyForJob(request):
    return render(request,'Applyforjob.html')

def myProfile(request):
    return render(request,'myProfile.html')


def view_job_details(request):
    job_details_list = Jobdetails.objects.all()
    return render(request, 'Applyforjob.html', {'job_details_list': job_details_list})

from django.shortcuts import render
from django.contrib.auth.models import User

def usernames_non_numeric(request):
    non_numeric_usernames = User.objects.exclude(username__regex=r'^\d').exclude(username='admin').exclude(username='KLU')
    return render(request, 'Scompanynames.html', {'usernames': non_numeric_usernames})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def apply_for_job(request, id):
        # Retrieve the job details based on the job_id
        job = Jobdetails.objects.get(pk=id)
        # Create a new application object with the retrieved job details and the logged-in user's information
        application = Application.objects.create(
            name=request.user.first_name,
            job_title=job.job_title,
            email=request.user.email
        )
        application.save()
        # Redirect to a success page after applying
        return redirect('apply')  # Replace 'success_page' with the URL name of your success page

from django.http import HttpResponse

def display_applications(request):
    # Fetch all Application instances
    print("Entered")
    applications = Application.objects.all()
    # Print the content of each application
    for application in applications:
        print(f"Name: {application.name}, Job Title: {application.job_title}, Email: {application.email}")

    # Return a simple HTTP response indicating success
    return HttpResponse("Applications printed in terminal.")

# views.py
from django.shortcuts import render
from .models import Application

def application_list(request, name):
    applications = Application.objects.filter(name=name)
    return render(request, 'sapplied.html', {'applications': applications})



def delete_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.method == 'POST':
        application.delete()
        return redirect('applied')