from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from cfoodapp.forms import *
from django.contrib.auth.models import User
#from auth_app.models import *
from cfoodapp.models import *
# Create your views here.

def login_cfood(request):
    if request.method == "POST":
        formulaire = CustomAuthenticationForm(request, data=request.POST)

        if formulaire.is_valid():
            username = formulaire.cleaned_data["username"]
            password = formulaire.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirection en fonction de l'université de l'utilisateur
                if hasattr(user, "universite"):  # Vérifie que le champ 'universite' existe
                    universite = user.universite
# Stocker les informations de l'utilisateur dans la session
                    request.session['user_profile'] = {
                        "username": user.username,
                        "nom": user.last_name,
                        "prenom": user.first_name,
                        "universite": user.universite,
                        "numero": user.numero,
                        "email": user.email
                    }
                    
                    if universite == "UPB":
                        return redirect("upbHome")
                    elif universite == "UIA":
                        return redirect("uiaHome")
                    else:
                        # Si l'université n'est ni UPB ni UIA, redirigez vers une page par défaut
                        return redirect("defaultHome")
                else:
                    # Si l'attribut 'universite' n'est pas défini, utilisez une redirection par défaut
                    return redirect("defaultHome")

            # Si l'utilisateur n'a pas pu être authentifié, afficher un message d'erreur
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")

    else:
        # Si la méthode n'est pas POST, créez un nouveau formulaire
        formulaire = CustomAuthenticationForm()

    return render(request, "login.html", {"formulaire": formulaire})


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
            niveau = formulaire.cleaned_data['niveau']
            filiere = formulaire.cleaned_data['filiere']
            annee_etude = formulaire.cleaned_data['annee_etude']
            mdp1 = formulaire.cleaned_data['password1']
    
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                return render(request, 'etudiant_inscription.html', {'formulaire': formulaire})

            else:
                utilisateur = formulaire.save(commit=False)
                #utilisateur.set_password(formulaire.cleaned_data['password1'])
                utilisateur.save()
                #util.save()
                #utilisateur.set_password(formulaire.cleaned_data['password1'])

                etudiant = Etudiant.objects.create(
                    user=utilisateur,
                    niveau=niveau,
                    filiere=filiere,
                    annee_etude=annee_etude
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
""" def login_cfood(request):
    #universite = Universite.nom
    if request.method == "POST":
        #universite = request.POST.get('universite')
        #username = request.POST['username']
        #pwd = request.POST['pwd']
        username = request.POST['username']
        pwd = request.POST['password']
        #authentifions l'utilisateur
        user = authenticate(request, username=username, password=pwd)
        #vefifions si l utilisateur est dans notre bd
        if user is not None:
            #si oui, l authentifier
            login(request, user)
            prenom = user.first_name
            nom = user.last_name
            nomUser = user.username

            return redirect("upbHome", username=nomUser)
            #messages.success(request, "Vous etes bien authenfifier!")
        #sinon
        else:
            messages.error(request, "Erreur d'authentification!")
            return render(request, "login.html")
    return render(request, "login.html") """

""" def login_cfood(request):
    if request.method == "POST":
        username = request.POST["username"]
        pwd = request.POST["password"]
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            #firstname = user.first_name
            return redirect("upb_home")  # Pas de paramètre passé
        else:
            messages.error(request, "Erreur d'authentification!")
    return render(request, "login.html") """



""" def login_cfood(request):
    if request.method == 'POST':
        formulaire = CustomAuthenticationForm(request, data=request.POST)
        if formulaire.is_valid():
            user = formulaire.get_user()
            login(request, user)  # Connecter l'utilisateur
            return redirect("upbHome")  # Rediriger après connexion réussie
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    else:
        formulaire = CustomAuthenticationForm()  # Formulaire vierge pour GET

    return render(request, "login.html", {'formulaire': formulaire}) """