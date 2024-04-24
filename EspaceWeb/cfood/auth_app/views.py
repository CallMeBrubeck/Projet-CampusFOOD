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
        username = request.POST['username']
        pwd = request.POST['pwd']
        #authentifions l'utilisateur
        user = authenticate(username=username, password=pwd)
        #vefifions si l utilisateur est dans notre bd
        #si l utilisateur existe et que sont univrrsite est UPB:
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




""" def signin(request):
    formulaire = InscriptionUtilisateur()
    if request.method == 'POST':
        form = InscriptionUtilisateur(request.POST)
        if form.is_valid():
            username = formulaire.cleaned_data['username']
            first_name = formulaire.cleaned_data['first_name'] 
            password = formulaire.cleaned_data['password']
            last_name = formulaire.cleaned_data['last_name']
            is_etudiant = formulaire.cleaned_data['is_etudiant']
            is_professeur = formulaire.cleaned_data['is_professeur']
            is_adminpersonnel = formulaire.cleaned_data['is_adminpersonnel']
            numero = formulaire.cleaned_data['numero']
            universite = formulaire.cleaned_data['universite']
            
            # Créer le nouvel utilisateur avec les données du formulaire
            utilisateur = CustomUser(username=username, first_name=first_name, last_name=last_name, password=password, is_etudiant=is_etudiant, is_professeur=is_professeur, is_adminpersonnel=is_adminpersonnel)
            #utilisateur = form.save()
            utilisateur.save()
            
            # Connexion automatique après l'inscription (optionnel)
            #login(request, utilisateur)
            
            # Redirection selon le type d'utilisateur
            if utilisateur.is_etudiant:
                return redirect('etudiant_inscription')  # Rediriger vers le tableau de bord étudiant
            elif utilisateur.is_professeur:
                return redirect('professeur_inscription')  # Rediriger vers le tableau de bord professeur
            elif utilisateur.is_adminpersonnel:
                return redirect('enseignant_inscription')  # Rediriger vers le tableau de bord administratif
            else:
                # Si aucun type n'est défini, redirigez vers une page générique
                return redirect('signin')
        else:
            messages.error(request, 'Il y a des erreurs dans le formulaire. Veuillez corriger et réessayer.')
    else:
        form = InscriptionUtilisateur()

    return render(request, 'signin.html',  {
        'name': 'Signin',
        'formulaire': formulaire})
 """



def etudiant(request):
    if request.method == 'POST':
        formulaire = EtudiantForm(request.POST)
        if formulaire.is_valid():
            # Vérifier s'il y a déjà un utilisateur avec le même nom d'utilisateur
            
            username = formulaire.cleaned_data.get('username', None)
            if username and CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                return render(request, 'etudiant_inscription.html', {'formulaire': formulaire})

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

