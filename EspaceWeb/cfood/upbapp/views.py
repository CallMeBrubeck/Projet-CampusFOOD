from django.shortcuts import render, redirect
from cfoodapp.models import *
from django.contrib.auth import logout
from django.contrib import messages

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



def logOut(request):
    #return render(request, 'app/logout.html')
    #appelons la fonction logout
    logout(request)
    messages.success(request,'Vous ave ete bien deconnecter')
    return redirect("home")

#=============================EndUPB page=============================
