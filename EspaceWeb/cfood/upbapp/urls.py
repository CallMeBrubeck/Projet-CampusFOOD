from django.urls import path, include
from upbapp.views import *

urlpatterns = [
    #=======================UPB_page===================
    path('', upb_page, name="upbHome"),  # Le paramètre 'username' est ici
    path('plat/<str:nom_plat>/', detail, name="detail"),
    #path('ajouter_au_panier', ajouter_au_panier, name='ajout'),
    path('add_to_cart', add_to_cart, name="add"),
    path('panier', cart, name="panier"),
    path('menu', menu, name="menu"),
    path('article/recherche', search, name="search"),
    #=======================EndUPB_page===================
]
