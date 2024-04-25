from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('',login_cfood, name="login"),
    path('signin',signin, name="signin"),
    path('etudiant_inscription', etudiant, name="etudiant_inscription"),
    path('personnel_inscription', personnel, name="personnel_inscription"),
    path('enseignant_inscription', enseignant, name="enseignant_inscription"),
    #Une fois connecter:
    #=======================UPB_page===================
    path('upb', upb_page, name="upbHome"),
    path('plat/<str:nom_plat>',detail, name="detail"),
    path('panier/', panier, name="panier"),
    path('menu/', menu, name="menu"),
    path('article/recherche',search, name="search" ),
    #=======================EndUPB_page===================

    
    ##=======================UIA_page===================
    path('uia', uia_page, name="uiaHome"),


]
