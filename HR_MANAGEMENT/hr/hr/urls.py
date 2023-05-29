"""hr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage, name="loginpage"), # url for login page  
    path('homepage/',views.homepage, name='homepage'), # url for home page  
    path('loginpage/',views.loginpage,name='loginpage'), # url for login page  
    path('logoutpage/',views.logout, name='logoutpage'),  
    path('empform',views.empform, name='form'), # url for empform page  
    path('empdetails',views.empdetails,name='details'), # url for empdetails page
       
]
