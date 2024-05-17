from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
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

@login_required
def logOut(request):
    #return render(request, 'app/logout.html')
    #appelons la fonction logout
    logout(request)
    messages.success(request,'Vous ave ete bien deconnecter')
    return redirect("home")