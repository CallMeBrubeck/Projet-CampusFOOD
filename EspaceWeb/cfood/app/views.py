from django.shortcuts import render

# Create your views here.

#fonction de l'acceuil
def acceuil_view(request):
    return render(request, 'aceuil.html')