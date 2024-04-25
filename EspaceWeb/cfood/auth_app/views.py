from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from cfoodapp.forms import *
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def login_cfood(request):
    #universite = Universite.nom
    if request.method == "POST":
        #universite = request.POST.get('universite')
        universite = request.POST['universite']
        username = request.POST['username']
        pwd = request.POST['pwd']
        #authentifions l'utilisateur
        user = authenticate(username=username, password=pwd, universite=universite)
        #vefifions si l utilisateur est dans notre bd
        #si l utilisateur existe et que sont univrrsite est UPB:
        if user is not None:
            #obtenir les utilisateur
            utilisateur=username
            #verifier si universite == UPB
            if universite == "UPB":
                #redirect("upbHome", {'nomUser':nomUser})
                return redirect("upbHome", nomUser=utilisateur)
            #verifier si universite == UIA
            elif universite=="UIA":
                return redirect("uiaHome", nomUser=utilisateur)
            #verifier si universite == UFHB
            elif universite=="UFHB":
                return redirect("ufhbHome", nomUser=utilisateur)
            
            else:
                return redirect("")
            #messages.success(request, "Vous etes bien authenfifier!")
            return redirect("home")
        #sinon
        else:
            messages.error(request, "Erreur d'authentification!")
            return render(request, "login.html")
    return render(request, "login.html")



def signin(request):
    if request.method == 'POST':
        type_utilisateur = request.POST.get('type_utilisateur')
        if type_utilisateur == 'Etudiant':
            return redirect('etudiant_inscription')
        elif type_utilisateur == 'Enseignant':
            return redirect('enseignant_inscription')
        elif type_utilisateur == "Personnel d'administration":
            return redirect('personnel_inscription')
    # ...autres types d'utilisateurs...
        else:
            messages.error(request, 'Entrez le champs correct!!!.')
    return render(request, 'signin.html', {
        'name': 'Signin'})



def etudiant(request):
    if request.method == 'POST':
        formulaire = EtudiantForm(request.POST)
        if formulaire.is_valid():
            # Vérifier s'il y a déjà un utilisateur avec le même nom d'utilisateur
            type_utilisateur = formulaire.cleaned_data['type_utilisateur']
            username = formulaire.cleaned_data['username']
            first_name = formulaire.cleaned_data['first_name']
            last_name = formulaire.cleaned_data['last_name']
            email = formulaire.cleaned_data['email']
            numero = formulaire.cleaned_data['numero']
            universite = formulaire.cleaned_data['universite']
            #niveau = formulaire.cleaned_data['niveau']
            #filiere = formulaire.cleaned_data['filiere']
            #annee_etude = formulaire.cleaned_data['annee_etude']
            mdp1 = formulaire.cleaned_data['password1']
            #users = CustomUser(username=username, first_name=first_name, last_name=last_name, email=email, numero=numero, universite=universite, password=mdp1)
            #username = formulaire.cleaned_data.get('username', None)
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                return render(request, 'etudiant_inscription.html', {'formulaire': formulaire})

            utilisateur = formulaire.save(commit=False)
            utilisateur.set_password(formulaire.cleaned_data['password1'])
            utilisateur.save()

            etudiant = Etudiant(
                user=utilisateur,
                niveau=formulaire.cleaned_data['niveau'],
                filiere=formulaire.cleaned_data['filiere'],
                annee_etude=formulaire.cleaned_data['annee_etude']
            )
            etudiant.save()

            messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
            return redirect('login')

    else:
        formulaire = EtudiantForm()

    return render(request, 'etudiant_inscription.html', {'formulaire': formulaire})

#formulaire d inscription d un enseignat

def enseignant(request):
    if request.method == 'POST':
        formulaire = EnseignantForm(request.POST)
        if formulaire.is_valid():
            # Vérifier si le nom d'utilisateur existe déjà
            username = formulaire.cleaned_data.get('username', None)
            if username and CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                return render(request, 'enseignant_inscription.html', {'formulaire': formulaire, 'name': 'Enseignant Inscription'})

            utilisateur = formulaire.save(commit=False)
            utilisateur.set_password(formulaire.cleaned_data['password1'])
            utilisateur.save()

            enseignant = Enseignant(
                user=utilisateur,
                matiere=formulaire.cleaned_data['matiere']
            )
            enseignant.save()

            messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
            return redirect('login')

    else:
        formulaire = EnseignantForm()

    return render(request, 'enseignant_inscription.html', {'formulaire': formulaire, 'name': 'Enseignant Inscription'})



#formulaire d inscription d un Personnel d administration


def personnel(request):
    if request.method == 'POST':
        formulaire = PersonnelAdminForm(request.POST)
        if formulaire.is_valid():
            # Vérifier s'il y a un nom d'utilisateur dupliqué
            username = formulaire.cleaned_data.get('username', None)
            if username and CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                return render(request, 'personnel_inscription.html', {'formulaire': formulaire, 'name': 'Personnel Inscription'})

            utilisateur = formulaire.save(commit=False)
            utilisateur.set_password(formulaire.cleaned_data['password1'])
            utilisateur.save()

            personnel = PersonnelAdministration(
                user=utilisateur,
                poste=formulaire.cleaned_data['poste']
            )
            personnel.save()

            messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
            return redirect('login')

    else:
        formulaire = PersonnelAdminForm()

    return render(request, 'personnel_inscription.html', {'formulaire': formulaire, 'name': 'Personnel Inscription'})



#LSES PAGE APRES CONNEXION

#
#=============================UPB page=============================
def upb_page(request):
    return render(request, "upbapp/home.html")



def menu(request):
    list_categorie = Categorie.objects.all()
    list_plat = Plat.objects.all()
    context = {
        "name": "Menu",
        "list_categorie": list_categorie,
        "list_plat": list_plat
        }
    return render(request, 'cfoodapp/menu.html', context)

def detail(request, nom_plat):
    plat = Plat.objects.get(nom=nom_plat)
    categorie = plat.categorie
    plat_en_relation = Plat.objects.filter(categorie=categorie)[:5]
    #context = {"article": article}
    return render(request, 'cfoodapp/detail.html',
                  {
                      "plat": plat,
                      "per": plat_en_relation,
                      "name":"Details"
                    }
                    )


def panier(request):
    return render(request, 'cfoodapp/panier.html', {"name":"Panier"})



#fonction de recherche
def search(request):
    query = request.GET["article"]
    liste_article = Plat.objects.filter(nom__icontains=query)
    return render(request, 'cfoodapp/search.html', {
        "liste_article":liste_article
        })

#=============================EndUPB page=============================


#UIA page
def uia_page(request):
    user = CustomUser.objects.all()
    user
    return render(request, "uiaapp/home.html")



