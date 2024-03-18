from django.contrib import admin
from django.urls import path
from appcfood import views

urlpatterns = [
    path('', views.acceuil, name='acceuil')
]
