from django.shortcuts import render, get_object_or_404
from .models import Jobdetails
# Create your views here.
def companyhomepage(request):
    return render(request,'companyhomepage.html')

def Postjob(request):
    return render(request,'Postjob.html')

#add jobdetails to db
from django.shortcuts import render, redirect, get_object_or_404
from .models import Jobdetails

def Postjob(request):
    return render(request, 'Postjob.html')

def Postjobdb(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        job_des = request.POST.get('job_des')
        job_req = request.POST.get('job_req')
        job_sal = request.POST.get('job_sal')  # Added job_sal
        work_loc = request.POST.get('work_loc')
        app_email = request.POST.get('app_email')

        job_details = Jobdetails(
            job_title=job_title,
            job_des=job_des,
            job_req=job_req,
            job_sal=job_sal,  # Added job_sal
            work_loc=work_loc,
            app_email=app_email,
        )
        job_details.save()
        return redirect('view_job_details')
    return render(request, 'Postjob.html')

def view_job_details(request):
    job_details_list = Jobdetails.objects.all()
    return render(request, 'ViewJobdetails.html', {'job_details_list': job_details_list})

def edit_jobpost(request, job_id):
    job_details = get_object_or_404(Jobdetails, id=job_id)
    if request.method == 'POST':
        job_details.job_title = request.POST.get('job_title')
        job_details.job_des = request.POST.get('job_des')
        job_details.job_req = request.POST.get('job_req')
        job_details.job_sal = request.POST.get('job_sal')  # Added job_sal
        job_details.work_loc = request.POST.get('work_loc')
        job_details.app_email = request.POST.get('app_email')
        job_details.save()
        return redirect('view_job_details')
    return render(request, 'edit_job.html', {'job_details': job_details})

def delete_jobdetails(request, job_id):
    job_details = get_object_or_404(Jobdetails, id=job_id)
    job_details.delete()
    return redirect('view_job_details')

from django.shortcuts import render
from django.contrib.auth.models import User

def usernames_with_numeric(request):
    numeric_usernames = User.objects.filter(username__regex=r'^\d')
    return render(request, 'cstudentnames.html', {'usernames': numeric_usernames})

from django.shortcuts import render
from student.models import Application

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'displayapplication.html', {'applications': applications})