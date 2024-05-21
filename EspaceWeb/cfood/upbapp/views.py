from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cfoodapp.models import *
from django.contrib.auth import logout
from django.contrib import messages
from cfoodapp.urls import *

#========pour creer le panier======
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
#=======end======================
# Create your views here.

#=============================UPB page=============================
@login_required
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

@login_required
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

@login_required
def categorieView(request, id):
    if request.user.is_authenticated:
        #ensuite creer ou obtenir son panier sil en avait deja nom completer(completed=False)
        cart, created = Panier.objects.get_or_create(user=request.user, completed=False)
        user_profile = request.session.get('user_profile', {})
        list_categorie = Categorie.objects.all()
        list_plat = Plat.objects.all()
        idcat = list_categorie.pk
    context = {
        "name": "Menu",
        "list_categorie": list_categorie,
        "user_profile": user_profile,
        "list_plat": list_plat,
        "cart":cart,
        "idcat":idcat
    }
    return render(request, "upbapp/menu.html", context)


@login_required
@login_required
def detail(request, nom_plat):
    user_profile = request.session.get('user_profile', {})
    plat = get_object_or_404(Plat, nom=nom_plat)
    list_categorie = Categorie.objects.all()
    categorie = plat.categorie
    plat_en_relation = Plat.objects.filter(categorie=categorie)[:5]

    commentaires = Avis.objects.filter(plat=plat).order_by('-date_poste')

    cart = None
    if request.user.is_authenticated:
        cart, created = Panier.objects.get_or_create(user=request.user, completed=False)

        if request.method == 'POST':
            form = CommentaireForm(request.POST)
            if form.is_valid():
                commentaire = form.save(commit=False)
                commentaire.user = request.user
                commentaire.plat = plat
                commentaire.save()
                return redirect('detail', nom_plat=plat.nom)
        else:
            form = CommentaireForm()

    context = {
        'user_profile': user_profile,
        'plat': plat,
        'per': plat_en_relation,
        'name': 'Details',
        'cart': cart,
        'list_categorie': list_categorie,
        'commentaires': commentaires,
        'form': form,
    }

    return render(request, 'upbapp/detail.html', context)

#============preparation du panier ===============
@login_required
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


@login_required
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
@login_required
def search(request):
    user_profile = request.session.get('user_profile', {})
    list_categorie = Categorie.objects.all()
    query = request.GET["article"]
    list_plat = Plat.objects.filter(nom__icontains=query)
    return render(request, 'upbapp/search.html', {
        "liste_article":list_plat, "list_categorie": list_categorie,"user_profile": user_profile,
        })


@login_required
def logOut(request):
    logout(request)
    #messages.success(request,'Vous ave ete bien deconnecter')   
    return redirect("home")
#=============================EndUPB page=============================

def admin_page(request):
    return render(request, "upbapp/admin.html")
