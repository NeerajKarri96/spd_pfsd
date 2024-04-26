from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.companyhomepage,name='companyhomepage'),
    path('jobpost',views.Postjob,name='jobpost'),
    path('jobpostdb',views.Postjobdb,name='post_job'),
    path('view',views.view_job_details,name='view_job_details'),
    path('edit_jobpost/<int:job_id>/', views.edit_jobpost, name='edit_jobpost'),
    path('delete_job/<int:job_id>/',views.delete_jobdetails,name='delete_job'),
    path('cstudentnames/',views.usernames_with_numeric,name='studentnames'),
    path('applicationss',views.application_list,name='application'),
]