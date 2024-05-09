from django.urls import path, include
from .views import *

urlpatterns = [
    path('',login_cfood, name="login"),
    #path('',logOut, name="logout"),
    path('signin',signin, name="signin"),
    path('etudiant_inscription', etudiant, name="etudiant_inscription"),
    path('personnel_inscription', personnel, name="personnel_inscription"),
    path('enseignant_inscription', enseignant, name="enseignant_inscription"),
    #Une fois connecter:
    #=======================UPB_page===================
    #path('upb/<str:firstname>/',include("upbapp.urls")),
    #=======================EndUPB_page===================
    #=======================UIA_page===================
]
