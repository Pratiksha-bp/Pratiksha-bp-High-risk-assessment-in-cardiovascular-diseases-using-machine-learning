from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.admin_registerPage, name="register"),
	path('login/', views.admin_loginPage, name="login"),  
	path('logout/', views.admin_logoutPage, name="logout"),

    path('', views.home, name="home"),
    path('doctor_view', views.doctor_view, name="doctor_view"),


]