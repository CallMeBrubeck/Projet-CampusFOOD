from django.contrib.auth.forms import UserCreationForm
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



""" class InscriptionUtilisateur(UserCreationForm):
    type_utilisateur = forms.ChoiceField(choices=TYPE_UTILISATEUR_CHOICES, required=True)
    class Meta:
        model = CustomUser  # Assuming Utilisateur is your user model
        fields = ['type_utilisateur']
        widget={
            #'type_utilisateur': forms.ChoiceField(attrs={'class': 'form-control'})
            #'type_utilisateur': forms.ChoiceField()
            'type_utilisateur': forms.Select(attrs={'class': 'form-control'})
            } """



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



        
""" class EtudiantForm(UserCreationForm):
    type_utilisateur = forms.CharField(required=False, initial="Etudiant", widget=forms.TextInput(attrs={'class': 'form-control'}))  # Valeur par défaut "etudiant"
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nom = forms.CharField( required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenoms = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    niveau = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    filiere = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    universite = forms.ChoiceField(choices=choix_universite, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Etudiant
        fields = ['type_utilisateur','username','nom', 'prenoms', 'email', 'niveau', 'filiere', 'universite', 'password']

 """
""" class PersonnelAdministrationForm(UserCreationForm):
    type_utilisateur = forms.CharField(required=False, initial="Personnel d'administration", widget=forms.TextInput(attrs={'class': 'form-control'}))  # Valeur par défaut "etudiant"
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nom = forms.CharField( required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenoms = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    poste = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = PersonnelAdministration
        fields = ['type_utilisateur','username','nom', 'prenoms', 'email', 'poste', 'universite', 'password']



class EnseignantForm(UserCreationForm):
    type_utilisateur = forms.CharField(required=False, initial="Enseignant", widget=forms.TextInput(attrs={'class': 'form-control'})) 
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nom = forms.CharField( required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenoms = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    matiere = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    universite = forms.ChoiceField(choices=choix_universite, required=True, widget=forms.SelectMultiple(choices=choix_universite,attrs={'class': 'form-control'}))
  # Changed to MultipleChoiceField
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Enseignant
        fields = ['type_utilisateur', 'username', 'nom', 'prenoms', 'email', 'matiere', 'universite', 'password',]
     """