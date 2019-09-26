from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneFormField
from django.db import models

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    phone_number=PhoneFormField(help_text='Contact PhoneNumber')
 

    class Meta:
        model=User
        fields=['username','email','phone_number','password1','password2']