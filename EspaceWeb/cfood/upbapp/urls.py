from django.urls import path
from upbapp.views import *

urlpatterns = [
    #=======================UPB_page===================
    path('', upb_page, name="upbHome"),  # Le paramètre 'username' est ici
    path('plat/<str:nom_plat>/', detail, name="detail"),
    path('add_to_cart', add_to_cart, name="add"),
    path('panier', cart, name="panier"),
    path('menu', menu, name="menu"),
    path('article/recherche', search, name="search"),
    path('logout',logOut, name="logout"),
    path("admin", admin_page, name="administreation"),
    #=======================EndUPB_page===================
]
