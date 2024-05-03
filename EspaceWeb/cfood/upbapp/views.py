from django.shortcuts import render
from cfoodapp.models import *
#========pour creer le panier======
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
#=======end======================
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

#============preparation du panier ===============
@csrf_exempt
@require_POST
def ajouter_au_panier(request):
    print("Vue 'ajouter_au_panier' appelée")  # Débogage
    try:
        data = json.loads(request.body)  # Assurez-vous que le JSON est valide
    except json.JSONDecodeError:
        return JsonResponse({"error": "Requête mal formée"}, status=400)  # Gérer l'erreur JSON
    
    plat_id = data.get("plat_id")
    if not plat_id:
        return JsonResponse({"error": "ID du plat manquant"}, status=400)  # Retourner une erreur si nécessaire
    
    plat = get_object_or_404(Plat, id=plat_id)  # Récupérer le plat
    
    panier = request.session.get("panier", {})
    if plat_id in panier:
        panier[plat_id] += 1
    else:
        panier[plat_id] = 1

    request.session["panier"] = panier  # Mettre à jour le panier dans la session

    return JsonResponse({"message": "Article ajouté au panier", "panier": panier})


def panier(request):
    list_categorie = Categorie.objects.all()
    panier = request.session.get("panier", {})
    plats = []

    # Récupérer les plats et calculer le prix total pour chaque article
    for plat_id, quantity in panier.items():
        plat = get_object_or_404(Plat, id=plat_id)  # Récupérer le plat
        prix_total = plat.prix * quantity  # Calcul du prix total
        plats.append({"plat": plat, "quantity": quantity, "prix_total": prix_total})

    return render(request, 'upbapp/panier.html', {"plats": plats, "name": "Panier", "list_categorie": list_categorie})
""" def panier(request):
    return render(request, 'upbapp/panier.html', {"name":"Panier"}) """


#=============end panier process =================================================


#fonction de recherche
def search(request):
    query = request.GET["article"]
    liste_article = Plat.objects.filter(nom__icontains=query)
    return render(request, 'upbapp/search.html', {
        "liste_article":liste_article
        })

#=============================EndUPB page=============================