from django.contrib import admin
from django.urls import path
from appcfood import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('menu/', views.menu, name='menu'),
    path('login/', views.login, name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" ce code: 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
va nous permettre d avoir acces a notre repertoir 
de media qui enregistre la photo des articles ajoutees
 """
