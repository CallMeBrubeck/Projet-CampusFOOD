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



class InscriptionUtilisateur(UserCreationForm):
    type_utilisateur = forms.ChoiceField(choices=TYPE_UTILISATEUR_CHOICES, required=True)
    class Meta:
        model = CustomUser  # Assuming Utilisateur is your user model
        fields = ['type_utilisateur']
        widget={
            #'type_utilisateur': forms.ChoiceField(attrs={'class': 'form-control'})
            #'type_utilisateur': forms.ChoiceField()
            'type_utilisateur': forms.Select(attrs={'class': 'form-control'})
            }



class EtudiantForm(UserCreationForm):
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


class PersonnelAdministrationForm(UserCreationForm):
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
    