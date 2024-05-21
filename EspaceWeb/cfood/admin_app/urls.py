from django.urls import path
from .views import *


urlpatterns = [
    path('',login_admin, name="login-admin"),
    path('dashboard', dashboard, name="dashboard"),
    path('my-articles', user_articles, name="my-articles"),
    path('ajouter-article', AddArticle.as_view(), name="ajouter-article"), #j ai utiliser une vue de class
    path('my-users', users, name="all-users"),
    path('my-etudiants', usersEtudiant, name="all-etudiants"),
    path('my-enseignants', usersEnseignant, name="all-enseignants"),
    path('my-personnel', usersPersonnel, name="all-personnels"),
    path('modifier-article/<int:pk>', UpdateArticle.as_view(), name="modifier-article"),
    path('supprimer-article/<int:pk>', DeleteArticle.as_view(), name="supprimer-article"), #root ppour l edit d un article qu on veut supprimer, tenir compte de l id """
    path('ajouter-etudiant', CreateEtudiant.as_view(), name="ajouter-etudiant"),
    path('modifier-etudiant/<int:pk>', UpdateEtudiant.as_view(), name="modifier-etudiant"), #root ppour l edit d un etudiant qu on veut modifier, tenir compte de l id
    path('supprimer-etudiant/<int:pk>', DeleteEtudiant.as_view(), name="supprimer-etudiant"), #root ppour l edit d un etudiant qu on veut supprimer, tenir compte de l id """
    path('ajouter-enseignant', CreateEnseignant.as_view(), name="ajouter-enseignant"),
    path('modifier-enseignant/<int:pk>', UpdateEnseignant.as_view(), name="modifier-enseignant"), #root ppour l edit d un enseignant qu on veut modifier, tenir compte de l id
    path('supprimer-enseignant/<int:pk>', DeleteEnseignant.as_view(), name="supprimer-enseignant"), #root ppour l edit d un enseignant qu on veut supprimer, tenir compte de l id """
    path('ajouter-personnel', CreatePersonnelAdmin.as_view(), name="ajouter-personnel"),
    path('modifier-personnel/<int:pk>', UpdatePersonnelAdmin.as_view(), name="modifier-personnel"), #root ppour l edit d un personnel qu on veut modifier, tenir compte de l id
    path('supprimer-personnel/<int:pk>', DeletePersonnelAdmin.as_view(), name="supprimer-personnel"), #root ppour l edit d un personnel qu on veut supprimer, tenir compte de l id """
   
   
    
]
