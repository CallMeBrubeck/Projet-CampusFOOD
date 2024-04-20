from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('',login_cfood, name="login"),
    path('signin',signin, name="signin"),
     path('etudiant_inscription', etudiant, name="etudiant_inscription"),
    path('personnel_inscription', personnel, name="personnel_inscription"),
    path('enseignant_inscription', enseignant, name="enseignant_inscription"),

]
