from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request, 'appcfood/welcome.html')
def menu(request):
    return render(request, 'appcfood/menu.html')
def login(request):
    return render(request, 'appcfood/login.html')