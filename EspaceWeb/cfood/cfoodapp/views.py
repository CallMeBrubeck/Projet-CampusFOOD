from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    list_categorie = Categorie.objects.all()
    list_plat = Plat.objects.all()
    context = {
        "name": "Acceuil",
        "list_categorie": list_categorie,
        "list_plat": list_plat
        }
    return render(request, 'cfoodapp/home.html', context)


def signin(request):
    return render(request, 'cfoodapp/signin.html', {
        'name': 'Signin'
    })

