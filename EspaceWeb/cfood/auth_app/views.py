from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from cfoodapp.forms import *
# Create your views here.

def login_cfood(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        #authentifions l'utilisateur
        user = authenticate(username=username, password=pwd)
        #vefifions si l utilisateur est dans notre bd
        #si l utilisateur existe:
        if user is not None:
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



#formulaire d inscription d un etudiant
def etudiant(request):
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
    return render(request, 'etudiant_inscription.html', {
        'formulaire': formulaire,
        'name': 'Etudiant Inscription'})

#formulaire d inscription d un enseignat
def enseignant(request):
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
    return render(request, 'enseignant_inscription.html', {
        'formulaire': formulaire,
        'name': 'Enseignant Inscription'})


#formulaire d inscription d un Personnel d administration
def personnel(request):
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
    return render(request, 'personnel_inscription.html', 
                  {'formulaire': formulaire,
                    'name': 'Personnel Inscription'})