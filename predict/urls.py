from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='predict'),
    path("doctor", views.doctor, name='doctor'),
    path("about", views.about, name='about'),
    path("disease", views.disease, name='disease'),
    path("sample", views.sample, name='sample'),
    path("predict_disease", views.predict_disease, name='predict_disease'),

    path("sample", views.sample, name='sample'),
    path("test", views.test, name='test'),
    path('diabetes_pre/', views.diabetes_pre, name='diabetesprediction'),

    # path("admin", views.admin, name='admin'),
    path("signup", views.handleSignup, name='handleSignup'),
    path("login", views.handleLogin, name='handleLogin'),
    path("logout", views.handleLogout, name='handleLogout'),


    # path("doctorSignup", views.doctorSignup, name="doctorSignup"),

    # path("disease_result", views.disease_result, name='disease_result'),
]