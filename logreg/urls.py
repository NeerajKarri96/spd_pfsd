from django.urls import path, include
from . import views
#test northing is real
#accoding to yt
urlpatterns = [
path('',views.home,name='home'),
path('first/',views.first,name='first'),
path('role/',views.role,name='role'),
path('studentsignup/',views.studentsignup,name='studentsignup'),
path('companysignup/',views.companysignup,name='companysignup'),
path('companysignupbend/',views.companyregister,name='companyregister'),
path('studentsignupbend/',views.studentregister,name='studentregister'),
path('logins/',views.logins,name='logins'),
path('logout/',views.logout,name='logout'),
]