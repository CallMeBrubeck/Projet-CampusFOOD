from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cfoodapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin/', views.signin, name="signin"),
]