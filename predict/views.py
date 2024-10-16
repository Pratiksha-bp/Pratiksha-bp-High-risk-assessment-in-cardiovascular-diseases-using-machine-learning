from unittest import result
from django.shortcuts import render,HttpResponse, redirect
# from django.contrib.auth.models import User
from .models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from .models import Doctor



# Create your views here.
def index(request):
    return render(request, 'index.html')

def doctor(request):
    return render(request, 'doctor.html')

def about(request):
    return render(request, 'about.html')

def sample(request):
    return render(request, 'sample.html')


# @login_required(login_url='handleLogin')
def disease(request):
    return render(request, 'disease_form.html')

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters 
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        address = request.POST['address']
        
        # Check for error inputs 
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('doctor')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('doctor')

        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('doctor')
        # Create user 
        # users = Users.objects.create_user(username, email, pass1)
        users = Users()
        users.username = username
        users.email = email
        users.pass1 = pass1
        users.fname = fname
        users.lname = lname
        users.phone = phone
        users.address = address
        users.save()
        messages.success(request, "Your account has been successfull created")
        return redirect('doctor')
    else:
        
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters 
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = Users.objects.filter(username=loginusername, pass1=loginpassword)

        if user:
            messages.success(request, "Successfully Loged In")
            return render(request, 'sample.html',{'user_auth':True,'username':loginusername})
        else:
            messages.error(request, "Invalid  Credentials, Please try again")
            return redirect('doctor')

        
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    # messages.success(request, "Successfully Loged Out")
    return redirect('predict')
    # return render(request, '/index.html')
    


    return HttpResponse('handleLogout')




# *****************/****************

import numpy as np
import pickle



def predict_disease(request):
    
    return render(request,"disease_result.html")












# Diabetes disease Prediction

    
# *****************/****************
import pickle

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt



def test(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())


@csrf_exempt
def diabetes_pre(request):
    

    return render(request,"diabetes_disease_result.html")
