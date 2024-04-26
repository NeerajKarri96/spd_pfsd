from django.urls import path, include
from . import views
#test northing is real
#accoding to yt
urlpatterns = [
path('',views.studenthomepage,name='studenthomepage'),
path('apply',views.view_job_details,name='apply'),
path('myProfile',views.myProfile,name='myProfile'),
path('companynames/', views.usernames_non_numeric, name='companyNames'),
path('applied/<int:id>/', views.apply_for_job, name='apply_for_job'),
path('printooo/',views.display_applications,name='printall'),
#path('applieds/<str:application_name>/',views.application_list,name='applied'),
path('applieds/<str:name>/', views.application_list, name='applied'),
path('delete/<int:application_id>/', views.delete_application, name='delete_application')
]