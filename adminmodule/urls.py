from django.contrib import admin
from django.urls import path, include
from . import views

#accoding to yt
urlpatterns = [
path('',views.adminhomepage,name='adminhomepage'),
path('view',views.view_job_details,name='Aview_job_details'),
path('delete_job/<int:job_id>/', views.delete_jobdetails, name='Adelete_job'),
path('Acompanynames/', views.usernames_non_numeric, name='AcompanyNames'),
path('Astudentnames/', views.usernames_with_numeric, name='AstudentNames'),
path('Sdelete/<int:user_id>/', views.delete_userSN, name='delete_user'),
path('Cdelete/<int:user_id>/', views.delete_userCN, name='Cdelete_user'),


]