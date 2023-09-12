from email.mime.text import MIMEText

from django.shortcuts import render
from polls import forms
import smtplib
from IPython.display import clear_output
import datetime
#initialising email sending

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
clear_output()
from_email = 'thedatascientist326@gmail.com'
smtp_object.login(from_email,'geqwrvtbvgfkaiaf')
def check_email(value):
    value = value.split('@')[-1]
    value = value.split('.')[0]
    providers = [
        "gmail",
        "yahoo",
        "outlook",
        "icloud",
        "aol",
        "protonmail",
        "zoho",
        "mail",
        "gmx",
        "yandex",
        "fastmail",
        "tutanota",
        "mail",
        "hushmail",
        "icloud",
        "mailinator",
        "comcast",
        "verizon",
        "att",
        "hotmail",
    ]
    if not (value in providers):
        return False
    else:
        return True

# Create your views here.

def index(request):
    form = forms.Email_newsletter()
    if request.method == "POST":
        email = str(request.POST["email"])
        # form = forms.Email_newsletter(request.POST)
        # if form.is_valid():
        if check_email(email):
            msg = "Subject: " + "New newsletter subscriber" + '\n' + email
            smtp_object.sendmail(from_email, "wassimhamraa@gmail.com", msg)
            clear_output()
        else: pass
    return render(request, "index.html", {"form": form})


def projects(request):
    if request.method == "POST":
        email = str(request.POST["email"])
        # form = forms.Email_newsletter(request.POST)
        # if form.is_valid():
        if check_email(email):
            msg = "Subject: " + "New newsletter subscriber" + '\n' + email
            smtp_object.sendmail(from_email, "wassimhamraa@gmail.com", msg)
            clear_output()
        else:
            pass
    return render(request, "projects.html")


def project_website(request):
    if request.method == "POST":
        email = str(request.POST["email"])
        # form = forms.Email_newsletter(request.POST)
        # if form.is_valid():
        if check_email(email):
            msg = "Subject: " + "New newsletter subscriber" + '\n' + email
            smtp_object.sendmail(from_email, "wassimhamraa@gmail.com", msg)
            clear_output()
        else:
            pass
    return render(request, "project_website.html")

def project_healthcenter(request):
    if request.method == "POST":
        email = str(request.POST["email"])
        # form = forms.Email_newsletter(request.POST)
        # if form.is_valid():
        if check_email(email):
            msg = "Subject: " + "New newsletter subscriber" + '\n' + email
            smtp_object.sendmail(from_email, "wassimhamraa@gmail.com", msg)
            clear_output()
        else:
            pass
    return render(request,"project_healthcenter.html")


def services(request):
    if request.method == "POST":
        email = str(request.POST["email"])
        # form = forms.Email_newsletter(request.POST)
        # if form.is_valid():
        if check_email(email):
            msg = "Subject: " + "New newsletter subscriber" + '\n' + email
            smtp_object.sendmail(from_email, "wassimhamraa@gmail.com", msg)
            clear_output()
        else:
            pass
    return render(request, "services.html")


def about(request):
    if request.method == "POST":
        email = str(request.POST["email"])
        # form = forms.Email_newsletter(request.POST)
        # if form.is_valid():
        if check_email(email):
            msg = "Subject: " + "New newsletter subscriber" + '\n' + email
            smtp_object.sendmail(from_email, "wassimhamraa@gmail.com", msg)
            clear_output()
        else:
            pass
    return render(request, "about.html")


def contact(request):
    form = forms.Message()
    if request.method == "POST":
        # form = forms.Message(request.POST)
        # if form.is_valid():
        #     form.save(commit=True)
        first_name = str(request.POST["fname"])
        last_name = str(request.POST["lname"])
        email = str(request.POST["email"])
        message = str(request.POST["message"])
        if check_email(email):
            subject = "Someone wants to contact you"
            message = f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nMessage: {message}"
            msg = MIMEText(message)
            msg["Subject"] = subject
            msg["From"] = from_email
            msg["To"] = "wassimhamraa@gmail.com"
            smtp_object.sendmail(from_email, "wassimhamraa@gmail.com", msg.as_string())
            clear_output()
        else:
            pass
    return render(request, "contact.html", {"form": form})


def under_development(request):
    if request.method == "POST":
        email = str(request.POST["email"])
        # form = forms.Email_newsletter(request.POST)
        # if form.is_valid():
        if check_email(email):
            msg = "Subject: " + "New newsletter subscriber" + '\n' + email

            smtp_object.sendmail(from_email, "wassimhamraa@gmail.com", msg)
            clear_output()
        else:
            pass
    return render(request, "under_development.html")
