from django.shortcuts import render

# Create your views here.

 
def iua_page(request):
    # Vous pouvez utiliser le paramètre 'nomUser' pour afficher des informations personnalisées
    return render(request, "iuaapp/home.html")