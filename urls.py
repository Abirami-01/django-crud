"""crud_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from vehicle import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home.as_view(),name="home"),
    path('add.html',views.add.as_view(),name="add"),
    path('retrieve.html',views.read.as_view(),name="read"),
    path('delete/<id>',views.delete_view.as_view()),
    path('update/<id>',views.update.as_view(),name="update"),
   
    
]
