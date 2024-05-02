from django.shortcuts import render
from cfoodapp.models import *
# Create your views here.

#=============================UPB page=============================

def upb_page(request):
    # Vous pouvez utiliser le paramètre 'nomUser' pour afficher des informations personnalisées
    list_categorie = Categorie.objects.all()
    user_profile = request.session.get('user_profile', {})
    return render(request, "upbapp/home.html", {
        'user_profile': user_profile,
        "name": "upbHome",
        "list_categorie": list_categorie,
        })


def menu(request):
    list_categorie = Categorie.objects.all()
    list_plat = Plat.objects.all()
    context = {
        "name": "Menu",
        "list_categorie": list_categorie,
        "list_plat": list_plat
        }
    return render(request, 'upbapp/menu.html', context)

def detail(request, nom_plat):
    plat = Plat.objects.get(nom=nom_plat)
    categorie = plat.categorie
    plat_en_relation = Plat.objects.filter(categorie=categorie)[:5]
    #context = {"article": article}
    return render(request, 'upbapp/detail.html',
                  {
                      "plat": plat,
                      "per": plat_en_relation,
                      "name":"Details"
                    }
                    )


def panier(request):
    return render(request, 'upbapp/panier.html', {"name":"Panier"})



#fonction de recherche
def search(request):
    query = request.GET["article"]
    liste_article = Plat.objects.filter(nom__icontains=query)
    return render(request, 'upbapp/search.html', {
        "liste_article":liste_article
        })

#=============================EndUPB page=============================