from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cfoodapp import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('signin/', views.signin, name="signin"),
    #path('login/', views.signin, name="login"),
    path('plat/<str:nom_plat>', views.detail, name="detail"),
    path('panier/', views.panier, name="panier"),
    path('menu/', views.menu, name="menu"),
    #path('etudiant_inscription/', views.etudiant, name="etudiant_inscription"),
    #path('personnel_inscription/', views.personnel, name="personnel_inscription"),
    #path('enseignant_inscription/', views.enseignant, name="enseignant_inscription"),
    #pour la recherche
    path('article/recherche',views.search, name="search" ),
    #authentification app
    path('auth/',include("auth_app.urls")),
]