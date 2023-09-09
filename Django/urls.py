"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from polls import views

urlpatterns = [
    path("",views.index,name="index"),
    path("home/",views.index,name="index"),
    path("projects/",views.projects,name="projects"),
    path("project_website/",views.project_website,name="project_website"),
    path("project_healthcenter/",views.project_healthcenter,name="project_healthcenter"),
    path("services/",views.services,name="services"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("admin/", admin.site.urls),
    path("under_developement/",views.under_development,name="under_development")
]
