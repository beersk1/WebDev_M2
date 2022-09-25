from django.urls import path
from . import views 

urlpatterns = [
     path('loginpage/',views.loginpage,name = 'loginpage'),
     path('signuppage/',views.signuppage,name = 'signuppage'),
     path('logout/',views.logoutpage,name = 'logoutpage'),

     
]
