from django.urls import path
from .views import *


urlpatterns = [
    path('',login_admin, name="login-admin"),
    path('dashboard', dashboard, name="dashboard"),
    path('my-articles', user_articles, name="my-articles"),
    path('ajouter-article', AddArticle.as_view(), name="ajouter-article"), #j ai utiliser une vue de class
    path('modifier-article/<int:pk>', UpdateArticle.as_view(), name="modifier-article"), #root ppour l edit d un article qu on veut modifier, tenir compte de l id
    path('supprimer-article/<int:pk>', DeleteArticle.as_view(), name="supprimer-article"), #root ppour l edit d un article qu on veut supprimer, tenir compte de l id """
   
    
]
