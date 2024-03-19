from django.shortcuts import render

# Create your views here.

def acceuil(request):
    return render(request, 'appcfood/acceuil.html')
def menu(request):
    return render(request, 'appcfood/menu.html')
def login(request):
    return render(request, 'appcfood/login.html')