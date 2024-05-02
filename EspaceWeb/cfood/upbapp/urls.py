from django.urls import path, include
from upbapp.views import *

urlpatterns = [
    #=======================UPB_page===================
    path('', upb_page, name="upbHome"),  # Le paramètre 'username' est ici
    path('plat/<str:nom_plat>/', detail, name="detail"),
    path('panier', panier, name="panier"),
    path('menu', menu, name="menu"),
    path('article/recherche', search, name="search"),
    #=======================EndUPB_page===================
]
