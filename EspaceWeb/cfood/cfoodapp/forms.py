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
    type_utilisateur = forms.ChoiceField(
        choices=CustomUser.TYPE_UTILISATEUR_CHOICES,
        initial='etudiant',
        widget=forms.RadioSelect(),
        disabled=True,
        label="Type d'utilisateur"
    )
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom d'utilisateur")
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Prénoms")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom de famille")
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
    numero = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Numéro de téléphone")
    universite = forms.ChoiceField(choices=CustomUser.choix_universite, widget=forms.Select(attrs={'class': 'form-control'}), label="Université")
    niveau = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Niveau")
    filiere = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Filière")
    annee_etude = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label="Année d'étude")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmez le mot de passe")

    class Meta:
        model = CustomUser
        fields = ['type_utilisateur', 'username', 'first_name', 'last_name', 'email', 'numero', 'universite', 'niveau', 'filiere', 'annee_etude', 'password1', 'password2']




class EnseignantForm(UserCreationForm):
    type_utilisateur = forms.ChoiceField(
        choices=CustomUser.TYPE_UTILISATEUR_CHOICES,
        initial='professeur',
        widget=forms.RadioSelect(),
        disabled=True,
        label="Type d'utilisateur"
    )
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom d'utilisateur")
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Prénoms")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom de famille")
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
    numero = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Numéro de téléphone")
    universite = forms.ChoiceField(choices=CustomUser.choix_universite, widget=forms.Select(attrs={'class': 'form-control'}), label="Université")
    matiere = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Matière enseignée")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmez le mot de passe")

    class Meta:
        model = CustomUser
        fields = ['type_utilisateur', 'username', 'first_name', 'last_name', 'email', 'numero', 'universite', 'matiere', 'password1', 'password2']




class PersonnelAdminForm(UserCreationForm):
    type_utilisateur = forms.ChoiceField(
        choices=CustomUser.TYPE_UTILISATEUR_CHOICES,
        initial='adminpersonnel',
        widget=forms.RadioSelect(),
        disabled=True,
        label="Type d'utilisateur"
    )
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom d'utilisateur")
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Prénoms")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom de famille")
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
    numero = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Numéro de téléphone")
    universite = forms.ChoiceField(choices=CustomUser.choix_universite, widget=forms.Select(attrs={'class': 'form-control'}), label="Université")
    poste = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Poste")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmez le mot de passe")

    class Meta:
        model = CustomUser
        fields = ['type_utilisateur', 'username', 'first_name', 'last_name', 'email', 'numero', 'universite', 'poste', 'password1', 'password2']



#formulaire d ajout d article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['nom', 'description', 'prix', 'image', 'categorie']
        labels = {
            'nom': 'Nom', 
            'description': 'Description', 
            'prix': 'Prix', 
            'image': 'Image', 
            'categorie': 'Categorie'
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'prix': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
        }



class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['commentaire']
        labels = {'commentaire':'Commentaire'}
        widgets = {
            'commentaire': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }