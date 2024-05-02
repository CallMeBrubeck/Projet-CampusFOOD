from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django import forms

choix_universite = (
        ('UPB', 'Université Polytechnique de Bingerville'),
        ('UIA', 'Institut Universitaire dAbidjan'),
        ('UNA', 'Université Nangui Abrogoua'),
        ('UFHB', 'Université Felix Houphouet Boigny'),
    )


TYPE_UTILISATEUR_CHOICES = (
        ('Etudiant', 'Etudiant'),
        ('PersonnelAdministratif', 'Personnel Administratif'),
        ('Enseignant', 'Enseignant'),
    )



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}), label="Nom d'utilisateur")
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Mot de passe")

    # Vous pouvez ajouter des validations supplémentaires ou des métadonnées ici
    class Meta:
        fields = ['username', 'password']



class InscriptionUtilisateur(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Nom d'utilisateur")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Prénoms")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Nom de famille")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Mot de passe")
    type_utilisateur = forms.ChoiceField(
        choices=TYPE_UTILISATEUR_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label="Type d'utilisateur"
    )
    numero = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Numero de Tel")
    universite = forms.ChoiceField(choices=choix_universite, required=True, widget=forms.Select(attrs={'class': 'form-control'}), label="Universite")
    class Meta:
        model = CustomUser
        # Les champs que vous souhaitez inclure dans le formulaire
        fields = ['username', 'first_name', 'last_name', 'type_utilisateur', 'numero', 'universite']


class EtudiantForm(UserCreationForm):
    # Champ pour indiquer le type d'utilisateur (étudiant par défaut)
    type_utilisateur = forms.ChoiceField(
        choices=CustomUser.TYPE_UTILISATEUR_CHOICES,
        initial='etudiant',
        widget=forms.RadioSelect()  # Pour avoir un bouton radio
    )
    
    # Champs spécifiques à l'utilisateur
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    universite = forms.ChoiceField(choices=CustomUser.choix_universite, widget=forms.Select(attrs={'class': 'form-control'}))
    
    # Champs spécifiques à l'étudiant
    niveau = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    filiere = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    annee_etude = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = [
            'type_utilisateur', 'username', 'first_name', 'last_name', 'email', 'numero', 
            'universite', 'niveau', 'filiere', 'annee_etude', 'password1', 'password2'
        ]




class EnseignantForm(UserCreationForm):
    # Champ pour indiquer le type d'utilisateur (par défaut, c'est "professeur")
    type_utilisateur = forms.ChoiceField(
        choices=CustomUser.TYPE_UTILISATEUR_CHOICES,
        initial='professeur',
        widget=forms.RadioSelect()  # Pour indiquer le type avec des boutons radio
    )
    
    # Champs pour le modèle CustomUser
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    universite = forms.ChoiceField(choices=CustomUser.choix_universite, widget=forms.Select(attrs={'class': 'form-control'}))
    
    # Champs pour le modèle Enseignant
    matiere = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = [
            'type_utilisateur', 'username', 'first_name', 'last_name', 'email', 'numero', 
            'universite', 'matiere', 'password1', 'password2'
        ]



class PersonnelAdminForm(UserCreationForm):
    # Champ pour indiquer le type d'utilisateur (ici c'est le personnel administratif)
    type_utilisateur = forms.ChoiceField(
        choices=CustomUser.TYPE_UTILISATEUR_CHOICES,
        initial='adminpersonnel',
        widget=forms.RadioSelect()  # On utilise des boutons radio pour sélectionner le type
    )

    # Champs pour le modèle CustomUser
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    universite = forms.ChoiceField(
        choices=CustomUser.choix_universite,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Champs pour le modèle PersonnelAdministration
    poste = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Champs de mot de passe
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = [
            'type_utilisateur', 'username', 'first_name', 'last_name', 'email', 'numero', 
            'universite', 'poste', 'password1', 'password2'
        ]