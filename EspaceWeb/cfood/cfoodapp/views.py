from django.shortcuts import render, redirect
#from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
""" def home(request):
    list_categorie = Categorie.objects.all()
    list_plat = Plat.objects.all()
    context = {
        "name": "Acceuil",
        "list_categorie": list_categorie,
        "list_plat": list_plat
        }
    return render(request, 'cfoodapp/home.html', context) """


def home(request):
    return render(request, 'cfoodapp/home.html', {
        "name": "Acceuil"})

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

#formulaire d inscription d un etudiant
""" from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EtudiantForm
from .models import Etudiant, CustomUser

def etudiant(request):
    if request.method == 'POST':
        formulaire = EtudiantForm(request.POST)
        if formulaire.is_valid():
            # Vérifier s'il y a déjà un utilisateur avec le même nom d'utilisateur
            username = formulaire.cleaned_data.get('username', None)
            if username and CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                return render(request, 'cfoodapp/etudiant_inscription.html', {'formulaire': formulaire})

            utilisateur = formulaire.save(commit=False)
            utilisateur.set_password(formulaire.cleaned_data['password1'])
            utilisateur.save()

            etudiant = Etudiant(
                user=utilisateur,
                niveau=formulaire.cleaned_data['niveau'],
                filiere=formulaire.cleaned_data['filiere']
            )
            etudiant.save()

            messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
            return redirect('login')

    else:
        formulaire = EtudiantForm()

    return render(request, 'cfoodapp/etudiant_inscription.html', {'formulaire': formulaire})

#formulaire d inscription d un enseignat

def enseignant(request):
    if request.method == 'POST':
        formulaire = EnseignantForm(request.POST)
        if formulaire.is_valid():
            # Vérifier si le nom d'utilisateur existe déjà
            username = formulaire.cleaned_data.get('username', None)
            if username and CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                return render(request, 'cfoodapp/enseignant_inscription.html', {'formulaire': formulaire, 'name': 'Enseignant Inscription'})

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

    return render(request, 'cfoodapp/enseignant_inscription.html', {'formulaire': formulaire, 'name': 'Enseignant Inscription'})



#formulaire d inscription d un Personnel d administration


def personnel(request):
    if request.method == 'POST':
        formulaire = PersonnelAdminForm(request.POST)
        if formulaire.is_valid():
            # Vérifier s'il y a un nom d'utilisateur dupliqué
            username = formulaire.cleaned_data.get('username', None)
            if username and CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                return render(request, 'cfoodapp/personnel_inscription.html', {'formulaire': formulaire, 'name': 'Personnel Inscription'})

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

    return render(request, 'cfoodapp/personnel_inscription.html', {'formulaire': formulaire, 'name': 'Personnel Inscription'})
 """


""" def etudiant(request):
    formulaire = EtudiantForm()
    if request.method == 'POST':
        formulaire = EtudiantForm(request.POST)
        if formulaire.is_valid():
        #recuperer les champs
            type_utilisateur = formulaire.cleaned_data['type_utilisateur']
            username = formulaire.cleaned_data['username']
            nom = formulaire.cleaned_data['nom']
            prenoms = formulaire.cleaned_data['prenoms']
            email = formulaire.cleaned_data['email']
            niveau = formulaire.cleaned_data['niveau']
            filiere = formulaire.cleaned_data['filiere']
            universite = formulaire.cleaned_data['universite']
            password = formulaire.cleaned_data['password']
      #verifier si l'utilisateur n existe pas
        if Etudiant.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')
            return redirect('etudiant_inscription')
      #sinon enregistre l'objet
        etudiant = Etudiant(type_utilisateur = type_utilisateur,username = username, nom = nom, prenoms = prenoms, email = email, niveau = niveau, filiere = filiere, universite = universite, password = password)
        etudiant.save()
        messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
        return redirect('login')
    return render(request, 'cfoodapp/etudiant_inscription.html', {
        'formulaire': formulaire,
        'name': 'Etudiant Inscription'})
 """


""" def enseignant(request):
    formulaire = EnseignantForm()
    if request.method == 'POST':
        formulaire = EnseignantForm(request.POST)
        if formulaire.is_valid():
      #recuperer les champs
            type_utilisateur = formulaire.cleaned_data['type_utilisateur']
            username = formulaire.cleaned_data['username']
            nom = formulaire.cleaned_data['nom']
            prenoms = formulaire.cleaned_data['prenoms']
            email = formulaire.cleaned_data['email']
            matiere = formulaire.cleaned_data['matiere']
            universite = formulaire.cleaned_data['universite']
            password = formulaire.cleaned_data['password']
            #verifier si l'utilisateur n existe pas
        if Enseignant.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')
            return redirect('enseignant_inscription')
            #sinon enregistre l'objet
        enseignant = Enseignant(
        type_utilisateur = type_utilisateur,
        username = username, 
        nom = nom, 
        prenoms = prenoms, 
        email = email, 
        matiere = matiere, 
        universite = universite, 
        password = password)
        enseignant.save()
        messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
        return redirect('login')
    return render(request, 'cfoodapp/enseignant_inscription.html', {
        'formulaire': formulaire,
        'name': 'Enseignant Inscription'}) """




""" def personnel(request):
    formulaire = PersonnelAdministrationForm()
    if request.method == 'POST':
        formulaire = PersonnelAdministrationForm(request.POST)
        if formulaire.is_valid():
        #recuperer les champs
            type_utilisateur = formulaire.cleaned_data['type_utilisateur']
            username = formulaire.cleaned_data['username']
            nom = formulaire.cleaned_data['nom']
            prenoms = formulaire.cleaned_data['prenoms']
            email = formulaire.cleaned_data['email']
            poste = formulaire.cleaned_data['poste']
            universite = formulaire.cleaned_data['universite']
            password = formulaire.cleaned_data['password']
        #verifier si l'utilisateur n existe pas
        if PersonnelAdministration.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')
            return redirect('personnel_inscription')
        #sinon enregistre l'objet
        personnel = PersonnelAdministration(
            type_utilisateur = type_utilisateur,
            username = username, 
            nom = nom, 
            prenoms = prenoms, 
            email = email, 
            poste = poste, 
            universite = universite, 
            password = password)
        personnel.save()
        messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
        return redirect('login')
    return render(request, 'cfoodapp/personnel_inscription.html', 
                  {'formulaire': formulaire,
                    'name': 'Personnel Inscription'}) """

#creons un formulaire de creation d un Utilisateur:

""" def signin(request):
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

    return render(request, 'cfoodapp/signin.html', {
        'name': 'Signin'}) """
















""" def signin(request):

    if request.method == 'POST':
        form = InscriptionUtilisateur(request.POST)
        if form.is_valid():
            if request.POST['type_utilisateur'] == 'Etudiant':
                formulaire = EtudiantForm(request.POST)
                if formulaire.is_valid():
                    #recuperer les champs
                    username = formulaire.cleaned_data['username']
                    nom = formulaire.cleaned_data['nom']
                    prenoms = formulaire.cleaned_data['prenoms']
                    email = formulaire.cleaned_data['email']
                    niveau = formulaire.cleaned_data['niveau']
                    filiere = formulaire.cleaned_data['filiere']
                    universite = formulaire.cleaned_data['universite']
                    password = formulaire.cleaned_data['password']
                    #verifier si l'utilisateur n existe pas
                    if Etudiant.objects.filter(username=username).exists():
                        messages.error(request, 'Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')
                        return redirect('signin')
                    #sinon enregistre l'objet
                    etudiant = etudiant(username = username, nom = nom, prenoms = prenoms, email = email, niveau = niveau, filiere = filiere, universite = universite, password = password)
                    etudiant.save()
            elif request.POST['type_utilisateur'] == 'PersonnelAdministratif':
                formulaire = PersonnelAdministrationForm(request.POST)
                if formulaire.is_valid():
                    #recuperer les champs
                    username = formulaire.cleaned_data['username']
                    nom = formulaire.cleaned_data['nom']
                    prenoms = formulaire.cleaned_data['prenoms']
                    email = formulaire.cleaned_data['email']
                    poste = formulaire.cleaned_data['poste']
                    universite = formulaire.cleaned_data['universite']
                    password = formulaire.cleaned_data['password']
                    #verifier si l'utilisateur n existe pas
                    if PersonnelAdministration.objects.filter(username=username).exists():
                        messages.error(request, 'Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')
                        return redirect('signin')
                    #sinon enregistre l'objet
                    personneladministratif = PersonnelAdministration(username = username, nom = nom, prenoms = prenoms, email = email, poste = poste, universite = universite, password = password)
                    personneladministratif.save()
            elif request.POST['type_utilisateur'] == 'Enseignant':
                formulaire = EnseignantForm(request.POST)
                if formulaire.is_valid():
                    #recuperer les champs
                    username = formulaire.cleaned_data['username']
                    nom = formulaire.cleaned_data['nom']
                    prenoms = formulaire.cleaned_data['prenoms']
                    email = formulaire.cleaned_data['email']
                    matiere = formulaire.cleaned_data['matiere']
                    universite = formulaire.cleaned_data['universite']
                    password = formulaire.cleaned_data['password']
                    #verifier si l'utilisateur n existe pas
                    if Enseignant.objects.filter(username=username).exists():
                        messages.error(request, 'Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')
                        return redirect('signin')
                    #sinon enregistre l'objet
                    enseignat = Enseignant(username = username, nom = nom, prenoms = prenoms, email = email, matiere = matiere, universite = universite, password = password)
                    enseignat.save()
    else:
        form = InscriptionUtilisateur()
        messages.error(request, 'Il y a des erreurs dans le formulaire. Veuillez corriger les erreurs.')
    return render(request, 'cfoodapp/signin.html', {
        'name': 'Signin',
        'form': form
    })


 """
