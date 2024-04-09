from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cfoodapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin/', views.signin, name="signin"),
    path('login/', views.signin, name="login"),
    path('etudiant_inscription/', views.etudiant, name="etudiant_inscription"),
    path('personnel_inscription/', views.personnel, name="personnel_inscription"),
    path('enseignant_inscription/', views.enseignant, name="enseignant_inscription"),
]