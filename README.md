# Projet : CFood(Campus FOOD)

### Membres

 * **KAMBIRE KOKO INNOCENT** [@CallMeBrubreck](https://github.com/CallMeBrubeck/)

 * SOGOBA EMMANUEL [@nazaga-tech](https://github.com/nazaga-tech/)

 * TRAORE MOUSSA [@MoussaTraor](https://github.com/MoussaTraor)

 * KOUASSI EMMANUEL [@manudev](https://github.com/manudev/)

 * KOUADIO SERI ANGE [@faveurdivine](https://github.com/faveurdivine/)

 ## DESCRIPTION

Dans le restaurant de l’UPB, et sans doute dans ceux des autres universités, certaines méthodes traditionnelles de gestion persistent. Une étude menée auprès d’un échantillon d’étudiants de l’UPB a révélé un certain nombre de critiques sur leur fonctionnement interne et sur la relation entre le personnel et les étudiants. Parmi ces critiques, on trouve :
- La gestion de façon traditionnelle (manuelle)
- Les longues files d’attente (enjeu sur le temps de service)
- Un manque de communication/interaction entre les étudiants et le personnel du restaurant sur leurs préférences
- Les retards dans le service
- Probleme de gestion de stock(le gaspillage alimentaire).

Ces problèmes ne sont probablement pas uniques à l’UPB. Ils pourraient également exister dans les autres universités de Côte d’Ivoire.
C’est dans cette optique que nous, étudiants de l’UPB, intervenons. Nous souhaitons apporter "la" solution informatique qu'est Cfood (Campus Food) pour faciliter la gestion des restaurants universitaires, non seulement à l’UPB, mais aussi dans toutes les universités de Côte d’Ivoire afin d’améliorer le rendement et la satisfaction de toutes les parties prenantes : étudiants, personnel du restaurant, administration, professeurs, et directeurs de restaurant.
Nous prévoyons une mise en œuvre progressive de notre solution, en commençant par une ou deux universités avant de l’étendre à d’autres. Cela nous permettra de tester notre solution, de résoudre les problèmes potentiels et d’apporter des améliorations avant une mise en œuvre à grande échelle.

## OBJECTIF GLOBAL

Nous avons identifié le besoin d'améliorer les services de notre restaurant universitaire ainsi que celui de certaines universités. Après six ans d'opération, il est temps d'innover et d'adopter des solutions numériques en phase avec le domaine d'expertise de l'université.
En d’autres termes, il s’agira de :
              CONCEVOIR ET REALISER UNE APPLICATION WEB ET MOBILE 
              DE RESTAURATION UNIVERSITAIRE

## OBJECTIFS SPECIFIQUE

Pour réaliser cet objectif global, plusieurs objectifs spécifiques doivent être atteints, qui sont les suivants :
-	Créer une interface facile à utiliser
-	Personnaliser l’interface et les fonctionnalités de l’application pour chaque université
-	Gerer les différents types d’utilisateur
-	Permettre les commandes en ligne
-	Fournir des informations sur les restaurants et les menus
-	Permettre aux utilisateurs de donner leur avis
-	Optimiser l'application pour le web et le mobile
-	Maintenir et mettre à jour l'application

## FONCTIONNALITES PRINCIPALES

### Utilisateurs Client :'Etudiants, PersonnelAdministration, Enseignant'
**fonctionnalités communes aux clients utilisateurs**

1. Authentification et gestion du profil :

- Création et modification de compte
- Connexion sécurisée
- Consultation et modification des informations personnelles
- Définition des préférences alimentaires (optionnel)

2. Consultation du menu :

- Accès aux menus du jour et de la semaine
- Affichage des photos et des descriptions des plats
- Filtrage par type de plat (entrée, plat principal, dessert) et par régime alimentaire (végétalien, sans gluten, etc.)
- Information sur les allergènes et les valeurs nutritives (optionnel)

3. Commande de plats :

- Ajout de plats au panier
- Choix de la quantité
- Validation de la commande
- Confirmation de la commande
  
4. Suivi des commandes :

- Visualisation de l'état de la commande en temps réel
- Notification de l'avancement de la préparation
  
5. Paiement sécurisé :

- Paiement en ligne via moyens de paiement (wave)
- Paiement en espèces au guichet (optionnel)
  
6. Annulation de commande :

- Possibilité d'annuler la commande avant sa préparation
- Remboursement automatique en cas d'annulation (optionnel)

7. Avis et commentaires :

- Notation des plats et du service
- Déposer des commentaires et des suggestions

**Fonctionnalité spécifique aux enseignants et au personnel de l'administration :**
#### Livraison à au bureau ou en salle des profs :

- Possibilité de se faire livrer la commande à son bureau ou en salle des profs
- Choix de l'heure de livraison


### Guichetier

1. Authentification et gestion des commandes :

- Connexion sécurisée à l'application
- Visualisation des commandes en cours et passées
- Filtrage des commandes par statut (en attente, en cours de préparation, prêtes)
- Accès aux détails de chaque commande (nom du client, plats commandés, mode de paiement, etc.)
  
2. Gestion des paiements :
  
- Encaissement des paiements en espèces
- Validation des paiements en ligne
- Remboursement des commandes annulées (optionnel)

3. Suivi de l'état des commandes :

- Marquage des commandes comme prêtes ou en cours de préparation
- Notification des clients lorsque la commande est prête

### Directeur du restaurant 

1. Authentification et gestion du compte :

- Création et modification du compte directeur
- Connexion sécurisée à l'application
- Déconnexion de l'application
- Modification du mot de passe
  
2. Accès au tableau de bord :

- Accès aux différents modules de l'application
  
3. Gestion du personnel :

- Ajout, modification et suppression des employés
- Définition des rôles et des permissions des employés
- Consultation des informations sur les employés

4. Gestion des commandes :

- Visualisation et validation des commandes en cours
- Suivi de l'état des commandes
- Remboursement des commandes annulées
  
5. Planification du menu :

- Création et modification des menus
- Définition des prix des plats
- Ajout et suppression de plats
- Gestion des stocks de plats et d'ingrédients
  
6. Gestion des demandes d'annulation :

- Accusé de réception des demandes d'annulation
- Approuver ou rejeter les demandes d'annulation
- Remboursement des commandes annulées
  
7. Traitement des avis :

- Consultation des avis des clients
- Réponse aux avis des clients
- Amélioration des services en fonction des avis

8. Gestion des informations sur le restaurant :

- Ajout, modification et suppression des informations sur le restaurant (nom, adresse, horaires d'ouverture, etc.)
- Définition des modes de paiement


### Administrateur systeme

1. Authentification et gestion du compte :

- Création et modification du compte administrateur
- Connexion sécurisée à l'application
- Déconnexion
- Modification du mot de passe
- 
2. Gestion des comptes utilisateurs :

- Création, modification et suppression des comptes utilisateurs (étudiants, enseignants, employées du restaurant)
- Définition des rôles et des permissions des utilisateurs
- Réinitialisation des mots de passe des utilisateurs
- Activation et désactivation des comptes utilisateurs
  
3. Gestion des informations sur les restaurants :

- Ajout, modification et suppression des restaurants
- Définition des horaires d'ouverture et de fermeture
- Ajout et modification des menus
- Gestion des stocks de plats et d'ingrédients
- Définition des prix des plats
