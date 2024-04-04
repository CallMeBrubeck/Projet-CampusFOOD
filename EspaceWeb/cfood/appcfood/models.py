from django.db import models
from PIL import Image

# Create your models here.
#model commande
class Commande(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id_commande = models.IntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.BooleanField()

    def __str__(self, date):
        return ()


#model Guichet
class Guichet(models.Model):    
    numero_guichet = models.CharField(max_length=15)
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=190)
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()

#Model Avis
class Avis(models.Model):
    #cle etrangere
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id = models.CharField(max_length=15)
    description = models.CharField(max_length=190)
    date_creation_avis = models.DateTimeField(auto_now_add=True)



#Model Emploee 
class Employe(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id = models.CharField(max_length=15)
    typ_utilisateur = models.BooleanField()
    nom = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    email = models.EmailField( max_length=254)
    adresse = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    date_embauche = models.DateTimeField(auto_now_add=True)
    salaire = models.IntegerField()


#model Facture
class Facture(models.Model):
    date_facturation = models.DateTimeField(auto_now_add=True)

    
#Model Guichetier
class Guichetier(Employe):
    #cle etrangere: la pk_ de la classe guichet
    guichet_id = models.ForeignKey(Guichet, on_delete=models.CASCADE)
    #cle etrangere: la pk_ de la classe commande, avis
    cmd_id = models.ForeignKey(Commande, on_delete=models.CASCADE)
    avis_id = models.ForeignKey(Avis, on_delete=models.CASCADE)
    facture_id = models.ForeignKey(Facture, on_delete=models.CASCADE)


#Model GestionCommande Par le Guichetier:
class GestionCommade(models.Model):
    cmd_id = models.ForeignKey(Commande, on_delete=models.CASCADE)
    guichetier_id = models.ForeignKey(Guichetier, on_delete = models.CASCADE)



#model Paiement
class Paiement(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id_paiement = models.IntegerField()
    mode_paiement = models.BooleanField()#Soit OM, Wave, MTN
    montant_payer = models.IntegerField()
    date_paiement = models.DateTimeField(auto_now_add=True)


#Model Utilisateurs
class Utilisateur(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id = models.CharField(max_length=15)
    typ_utilisateur = models.BooleanField()
    nom = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=100)
    date_ouverture_compte = models.DateTimeField()
    #cle etrangere: la pk_ de la classe Avis, Commande
    avis_id = models.ForeignKey(Avis, on_delete=models.CASCADE)
    cmd_id = models.ForeignKey(Commande, on_delete=models.CASCADE)
    paiement_id = models.ForeignKey(Paiement, on_delete=models.CASCADE)

    




#Trois type d'ulisateurs
    #A
class Etudiant(Utilisateur):
    filiere = models.CharField(max_length=15)
    niveau = models.CharField(max_length=15)

    #B
class Enseignant(Utilisateur):
    maitere = models.CharField(max_length=15)
    #C

class Administration(Utilisateur):
    poste = models.CharField(max_length=15)




#Model Universite
class Universite(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id = models.CharField(max_length=15)
    nom = models.CharField(max_length=50)
    localisation = models.CharField(max_length=50)




#Model Restaurant
class Restaurant(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id = models.CharField(max_length=15)
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=190)
    localisation = models.CharField(max_length=50)
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()
    #cle etrangere: la pk_ de la classe Employee et Universite
    employe_id = models.ForeignKey(Employe, on_delete=models.CASCADE)
    universite_id = models.ForeignKey(Universite, on_delete=models.CASCADE)





#Model des deux types d enployee
class DirecteurRestaurant(Employe):
    restau_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)



#model Plat
class Plat(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id = models.CharField(max_length=15)
    nom = models.CharField(max_length=50)
    prix_unitaire = models.IntegerField()
    image = models.ImageField( upload_to="images", height_field=None, width_field=None, max_length=None)
    date_creation = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=190)





#Model menu
class Menu(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id = models.CharField(max_length=15)
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=190)
    id_plat = models.ForeignKey(Plat, on_delete=models.CASCADE)





#Model Categorie
class Categorie(models.Model):
    #Pas d'id car avec django, _a se fait automatiquement lors de la creation ndune classe avec autofield
    # id = models.CharField(max_length=15)
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=190)
    id_plat = models.ForeignKey(Plat, on_delete=models.CASCADE)

    



#PlatCommandes: resulatant de la relation plusieur aplusieurs
    
class PlatCommander(models.Model):
    heure_commande = models.DateTimeField(auto_now_add=True)
    cmd_id = models.ForeignKey(Commande, on_delete=models.CASCADE)
    plat_id = models.ForeignKey(Plat, on_delete=models.CASCADE)


""" Pour demain on va mettre les fonctions :
def __str__ comme getter pour avoir les inforamtion sur chaques model """