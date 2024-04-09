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
        model = Utilisateur  # Assuming Utilisateur is your user model
        fields = ['type_utilisateur']
        widget={
            #'type_utilisateur': forms.ChoiceField(attrs={'class': 'form-control'})
            #'type_utilisateur': forms.ChoiceField()
            'type_utilisateur': forms.Select(attrs={'class': 'form-control'})
            }



class EtudiantForm(UserCreationForm):
    type_utilisateur = forms.CharField(required=False, initial="Etudiant")  # Valeur par défaut "etudiant"
    username = forms.CharField(required=True)
    nom = forms.CharField( required=True)
    prenoms = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    niveau = forms.CharField(required=True)
    filiere = forms.CharField(required=True)
    universite = forms.ChoiceField(choices=choix_universite, required=True)
    password = forms.PasswordInput()

    class Meta:
        model = Etudiant
        fields = ['type_utilisateur','username','nom', 'prenoms', 'email', 'niveau', 'filiere', 'universite', 'password']
        widgets = {
            'type_utilisateur': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenoms': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'niveau': forms.TextInput(attrs={'class': 'form-control'}),
            'filiere': forms.TextInput(attrs={'class': 'form-control'}),
            'universite': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class PersonnelAdministrationForm(UserCreationForm):
    type_utilisateur = forms.CharField(required=False, initial="Personnel d'administration")  # Valeur par défaut "etudiant"
    username = forms.CharField(required=True)
    nom = forms.CharField(required=True)
    prenoms = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    poste = forms.CharField(required=True)
    universite = forms.ChoiceField(choices=choix_universite, required=True)
    password = forms.PasswordInput()

    class Meta:
        model = PersonnelAdministration
        fields = ['type_utilisateur','username','nom', 'prenoms', 'email', 'poste', 'universite', 'password']
        widgets = {
            'type_utilisateur': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenoms': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'poste': forms.TextInput(attrs={'class': 'form-control'}),
            'universite': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class EnseignantForm(UserCreationForm):
    type_utilisateur = forms.CharField(required=False, initial="Enseignant")  # Valeur par défaut "etudiant"
    username = forms.CharField(required=True)
    nom = forms.CharField(required=True)
    prenoms = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    matiere = forms.CharField(required=True)
    universite = forms.MultipleChoiceField(choices=choix_universite, required=True)  # Changed to MultipleChoiceField
    password = forms.PasswordInput()

    class Meta:
        model = Enseignant
        fields = ['type_utilisateur', 'username', 'nom', 'prenoms', 'email', 'matiere', 'universite', 'password',]
        widgets = {
            'type_utilisateur': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenoms': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'matiere': forms.TextInput(attrs={'class': 'form-control'}),
            'universite': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }

    