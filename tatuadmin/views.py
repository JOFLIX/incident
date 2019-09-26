from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def admin_home(request):
    return render(request,'tatuadmin/admin_home.html')