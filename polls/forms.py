from django import forms
from django.core import validators
from polls.models import Visitor,Newsletter


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
        raise forms.ValidationError("email provider not registered")


class Message(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'fname'}))
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'lname'})
    )
    email = forms.EmailField(validators=[check_email],
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)])


    class Meta:
        model = Visitor
        fields = '__all__'
        widgets = {
            "message": forms.Textarea(
                attrs={'class': 'form-control', 'id': 'message', 'cols': 30, 'rows': 10})
        }
class Email_newsletter(forms.ModelForm):
    email = forms.EmailField(validators=[check_email],
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder':'Enter your email'}))
    class Meta:
        model = Newsletter
        fields = "__all__"
