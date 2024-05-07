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
    if request.user.is_authenticated:
        #ensuite creer ou obtenir son panier sil en avait deja nom completer(completed=False)
        cart, created = Panier.objects.get_or_create(user=request.user, completed=False)
    # Vous pouvez utiliser le paramètre 'nomUser' pour afficher des informations personnalisées
    list_categorie = Categorie.objects.all()
    user_profile = request.session.get('user_profile', {})
    return render(request, "upbapp/home.html", {
        'user_profile': user_profile,
        "name": "upbHome",
        "list_categorie": list_categorie,
        "cart":cart,
        })


def menu(request):
    if request.user.is_authenticated:
        #ensuite creer ou obtenir son panier sil en avait deja nom completer(completed=False)
        cart, created = Panier.objects.get_or_create(user=request.user, completed=False)
    user_profile = request.session.get('user_profile', {})
    list_categorie = Categorie.objects.all()
    list_plat = Plat.objects.all()
    context = {
        "name": "Menu",
        "list_categorie": list_categorie,
        "user_profile": user_profile,
        "list_plat": list_plat,
        "cart":cart
        }
    return render(request, 'upbapp/menu.html', context)

def detail(request, nom_plat):
    user_profile = request.session.get('user_profile', {})
    plat = Plat.objects.get(nom=nom_plat)
    categorie = plat.categorie
    plat_en_relation = Plat.objects.filter(categorie=categorie)[:5]
    if request.user.is_authenticated:
        #ensuite creer ou obtenir son panier sil en avait deja nom completer(completed=False)
        cart, created = Panier.objects.get_or_create(user=request.user, completed=False)
    #context = {"article": article}
    return render(request, 'upbapp/detail.html',
                  {
                    'user_profile': user_profile,
                    "plat": plat,
                    "per": plat_en_relation,
                    "name":"Details", 
                    "cart":cart
                    }
                    )

#============preparation du panier ===============
def add_to_cart(request):
    data = json.loads(request.body)
    #b-recuperons les id
    product_id = data["id"]
    #c-maintenant on va prendre l article qui correcpont a l id envoyer 
    product = Plat.objects.get(id=product_id)
    #d- verifier si un utilisateur est authentifier, car la seul contition pour ajouter dans panier
    if request.user.is_authenticated:
        cart, created = Panier.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = PanierItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity+=1
        cartitem.save()
        #on cree cette ligne pour que l mise a jour de qqt dans panier se fasse automatiquemet et non a un reload
        num_of_item = cart.num_of_items #aller voir dans script.js ligne 42

        print(cartitem)
    return JsonResponse(num_of_item, safe=False)


def cart(request):
    cart = None
    cartitems = []
    user_profile = request.session.get('user_profile', {})
    list_categorie = Categorie.objects.all()
    #on verifie si on a un user qui est connecter, puis:
    if request.user.is_authenticated:
        #ensuite creer ou obtenir son panier sil en avait deja nom completer(completed=False)
        cart, created = Panier.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()#ici on a utiliser le related_name='cartitems' du model pour avoir le panier correspondant au articles items du parent panier

    context = {"cart":cart, "items":cartitems, "name":"Panier", "list_categorie": list_categorie,"user_profile": user_profile,}
    return render(request, 'upbapp/panier.html', context)


#=============end panier process =================================================


#fonction de recherche
def search(request):
    user_profile = request.session.get('user_profile', {})
    list_categorie = Categorie.objects.all()
    query = request.GET["article"]
    liste_article = Plat.objects.filter(nom__icontains=query)
    return render(request, 'upbapp/search.html', {
        "liste_article":liste_article, "list_categorie": list_categorie,"user_profile": user_profile,
        })

#=============================EndUPB page=============================

""" @csrf_exempt
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
 """