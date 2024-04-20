from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(max_length=250)


    def __str__(self):
        return f"{self.nom}"



class Plat(models.Model):
    #idPlat = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.FloatField(max_length=8)
    image = models.ImageField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom} ({self.categorie.nom})"



class CustomUser(AbstractUser):
    is_etudiant = models.BooleanField(default=False)
    is_adminpersonnel = models.BooleanField(default=False)
    is_professeur = models.BooleanField(default=False)
    numero = models.CharField(max_length=15)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    def __str__(self):
        return f"{self.username}"
    

        



class Universite(models.Model):
    choix_universite = (
        ('UPB', 'Université Polytechnique de Bingerville'),
        ('UIA', 'Institut Universitaire dAbidjan'),
        ('UNA', 'Université Nangui Abrogoua'),
        ('UFHB', 'Université Felix Houphouet Boigny'),
    )
    nom = models.CharField(max_length=255, choices=choix_universite)
    adresse = models.CharField(max_length=255)
    site_web = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.nom}"



class Restaurant(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    capacite = models.IntegerField()
    horaires_ouverture = models.TimeField()
    horaires_fermeture = models.TimeField()
    universite = models.ForeignKey(Universite, on_delete=models.CASCADE)

    def __str__(self):
        return f"Restaurant: {self.nom} de luniversite : ({self.universite})"



class Menu(models.Model):
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Periode du Menu: {self.date} - du restaurant : {self.restaurant}"



class Employe(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    date_embauche = models.DateTimeField(auto_now_add=True)
    salaire = models.DecimalField(max_digits=6, decimal_places=2)
    type_employe = models.CharField(max_length=255, choices=[
        ('Guichetier', 'Guichetier'),
        ('Directeur Restaurant', 'Directeur Restaurant'),
    ])

    def __str__(self):
        return f"{self.nom} {self.prenoms} ({self.type_employe})"




class Etudiant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    niveau = models.CharField(max_length=255)
    filiere = models.CharField(max_length=255)
    annee_etude = models.IntegerField()
    universite = models.ForeignKey(Universite, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nom utilisateur {self.user.username} - Nom {self.user.first_name} - Niveau {self.niveau}"



class PersonnelAdministration(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    poste = models.CharField(max_length=255)
    universite = models.ForeignKey(Universite, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nom utilisateur {self.user.username} - Nom {self.user.first_name} - Poste {self.poste}"
    


class Enseignant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    matiere = models.CharField(max_length=255)
    universites = models.ManyToManyField(Universite)#car peut enseigner dans plusieurs universites
    def __str__(self):
        return f"Nom utilisateur {self.user.username} - Nom {self.user.first_name} - Matière {self.matiere}"



class Commande(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    montant_total = models.DecimalField(max_digits=6, decimal_places=2)
    statut = models.CharField(max_length=255, choices=[
        ('En cours', 'En cours'),
        ('Validée', 'Validée'),
        ('Annulée', 'Annulée'),
    ])

    def __str__(self):
        return f"{self.etudiant} - {self.restaurant} - {self.date} - {self.heure}"



class Facture(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    numero_facture = models.CharField(max_length=255)
    date_facturation = models.DateField()
    montant_total = models.DecimalField(max_digits=6, decimal_places=2)
    mode_paiement = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.numero_facture} - {self.commande}"



class Avis(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE, null=True, blank=True)
    note = models.IntegerField(choices=[
        (1, "1 étoile"),
        (2, "2 étoiles"),
        (3, "3 étoiles"),
        (4, "4 étoiles"),
        (5, "5 étoiles"),
    ])
    commentaire = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.note} - {self.commentaire}"



class Guichet(models.Model):
    numero = models.AutoField(primary_key=True)
    etat = models.CharField(max_length=255, choices=[
        ('Ouvert', 'Ouvert'),
        ('Fermé', 'Fermé'),
    ])
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, null=True, blank=True)
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()

    def __str__(self):
        return f"{self.numero} - {self.etat}"



class Paiement(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    methode = models.CharField(max_length=255, choices=[
        ('Espèce', 'Espèce'),
        ('Wave', 'Wave'),
    ])
    date_paiement = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.montant} - {self.methode} - {self.date_paiement}"
