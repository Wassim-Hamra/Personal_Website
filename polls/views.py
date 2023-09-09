from django.shortcuts import render
from polls import forms


# Create your views here.

def index(request):
    form = forms.Email_newsletter()
    if request.method == "POST":
        form = forms.Email_newsletter(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, "index.html", {"form": form})


def projects(request):
    return render(request, "projects.html")


def project_website(request):
    return render(request, "project_website.html")

def project_healthcenter(request):
    return render(request,"project_healthcenter.html")


def services(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    form = forms.Message()
    if request.method == "POST":
        form = forms.Message(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, "contact.html", {"form": form})


def under_development(request):
    return render(request, "under_development.html")
