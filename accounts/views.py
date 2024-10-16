from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm
# from .forms import OrderForm, CreateUserForm
# from .filters import OrderFilter
# Create your views here.

from predict.models import Users

def admin_registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def admin_loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def admin_logoutPage(request):
	logout(request)
	return redirect('/')


# @login_required(login_url='login')
# def home(request):

# 	return render(request, 'accounts/dashboard.html')


@login_required(login_url='login')
def home(request):
	# orders = Order.objects.all()
	# customers = Customer.objects.all()
	# users = Users.objects.all()

	# total_customers = customers.count()

	# total_orders = orders.count()
	# delivered = orders.filter(status='Delivered').count()
	# pending = orders.filter(status='Pending').count()

	# context = {'orders':orders, 'customers':customers,
	# 'total_orders':total_orders,'delivered':delivered,
	# 'pending':pending, 'users':users}
	# context = {'users':users}

	return render(request, 'accounts/dashboard.html')


@login_required(login_url='login')
def doctor_view(request):
	users = Users.objects.all()
	context = {'users':users}

	return render(request, 'accounts/doctor.html', context)
	# return redirect('doctor_view')

