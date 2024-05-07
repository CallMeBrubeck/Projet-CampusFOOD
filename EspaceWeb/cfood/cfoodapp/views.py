from django.shortcuts import render, redirect
#from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'cfoodapp/home.html', {
        "name": "Acceuil"})


#fonction de recherche
def search(request):
    query = request.GET["article"]
    liste_article = Plat.objects.filter(nom__icontains=query)
    context = {
        "liste_article":liste_article
        }
    return render(request, 'cfoodapp/search.html', context)
