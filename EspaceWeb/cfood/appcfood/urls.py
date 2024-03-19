from django.contrib import admin
from django.urls import path
from appcfood import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('menu/', views.menu, name='menu'),
    path('login', views.login, name='login'),
]
