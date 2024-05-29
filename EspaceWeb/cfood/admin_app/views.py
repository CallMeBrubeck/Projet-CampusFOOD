from django.shortcuts import render, redirect
from cfoodapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from cfoodapp.forms import *
from django.urls import reverse_lazy

# Create your views here.


def login_admin(request):
    formulaire = CustomAuthenticationForm()
    if request.method == "POST":
        formulaire = CustomAuthenticationForm(request, data=request.POST)

        if formulaire.is_valid():
            username = formulaire.cleaned_data["username"]
            password = formulaire.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    messages.error(request, "Vous n'avez pas les droits d'administration.")
        else:
            # Si la méthode n'est pas POST, créez un nouveau formulaire
            formulaire = CustomAuthenticationForm()
    return render(request, "partials/login.html", {"formulaire": formulaire})

@login_required
def dashboard(request):
    context = {
        'total_users': CustomUser.objects.count(),
        'total_etudiants': CustomUser.objects.filter(type_utilisateur='etudiant').count(),
        'total_enseignants': CustomUser.objects.filter(type_utilisateur='enseignant').count(),
        'total_personnel': CustomUser.objects.filter(type_utilisateur='personnel_administratif').count(),
        'total_plats': Plat.objects.count(),
        'total_universites': Universite.objects.count(),
        'total_restaurants': Restaurant.objects.count(),
        'total_employes': Employe.objects.count(),
    }
    return render(request, "db.html", context)


#fonction pour avoir acces aux article dans notre admin
@login_required
def user_articles(request):
    # Vérifiez si l'utilisateur est superutilisateur
    if not request.user.is_superuser:
        # Redirigez les utilisateurs non superutilisateurs vers la page d'accueil
        return redirect("home")

    # Récupérez tous les articles de la base de données
    list_articles = Plat.objects.all()
    return render(request, "db_objects/my-articles.html", {"list_articles": list_articles})


@login_required
def users(request):
    if not request.user.is_superuser:
        # Redirigez les utilisateurs non superutilisateurs vers la page d'accueil
        return redirect("home")
    list_user = CustomUser.objects.all()
    list_etudiant = Etudiant.objects.all()
    list_persAdmin = PersonnelAdministration.objects.all()
    list_enseignant = Enseignant.objects.all()
    context = {
        "utilisateurs": list_user,
        "etudiants": list_etudiant,
        "administrations": list_persAdmin,
        "enseignants": list_enseignant,
        'total_users': CustomUser.objects.count(),
        'total_etudiants': CustomUser.objects.filter(type_utilisateur='etudiant').count(),
        'total_enseignants': CustomUser.objects.filter(type_utilisateur='enseignant').count(),
        'total_personnel': CustomUser.objects.filter(type_utilisateur='personnel_administratif').count(),
        'total_plats': Plat.objects.count(),
        'total_universites': Universite.objects.count(),
        'total_restaurants': Restaurant.objects.count(),
        'total_employes': Employe.objects.count(),
    }
    return render(request, "db_objects/all-users.html", context)

@login_required
def usersEtudiant(request):
    if not request.user.is_superuser:
        # Redirigez les utilisateurs non superutilisateurs vers la page d'accueil
        return redirect("home")
    list_user = CustomUser.objects.all()
    list_etudiant = Etudiant.objects.all()
    list_persAdmin = PersonnelAdministration.objects.all()
    list_enseignant = Enseignant.objects.all()
    context = {
        "utilisateurs": list_user,
        "etudiants": list_etudiant,
        "administrations": list_persAdmin,
        "enseignants": list_enseignant,
        'total_users': CustomUser.objects.count(),
        'total_etudiants': CustomUser.objects.filter(type_utilisateur='etudiant').count(),
        'total_enseignants': CustomUser.objects.filter(type_utilisateur='enseignant').count(),
        'total_personnel': CustomUser.objects.filter(type_utilisateur='personnel_administratif').count(),
        'total_plats': Plat.objects.count(),
        'total_universites': Universite.objects.count(),
        'total_restaurants': Restaurant.objects.count(),
        'total_employes': Employe.objects.count(),
    }
    return render(request, "db_objects/db-etudiants.html", context)

@login_required
def usersPersonnel(request):
    if not request.user.is_superuser:
        # Redirigez les utilisateurs non superutilisateurs vers la page d'accueil
        return redirect("home")
    list_user = CustomUser.objects.all()
    list_etudiant = Etudiant.objects.all()
    list_persAdmin = PersonnelAdministration.objects.all()
    list_enseignant = Enseignant.objects.all()
    context = {
        "utilisateurs": list_user,
        "etudiants": list_etudiant,
        "administrations": list_persAdmin,
        "enseignants": list_enseignant,
        'total_users': CustomUser.objects.count(),
        'total_etudiants': CustomUser.objects.filter(type_utilisateur='etudiant').count(),
        'total_enseignants': CustomUser.objects.filter(type_utilisateur='enseignant').count(),
        'total_personnel': CustomUser.objects.filter(type_utilisateur='personnel_administratif').count(),
        'total_plats': Plat.objects.count(),
        'total_universites': Universite.objects.count(),
        'total_restaurants': Restaurant.objects.count(),
        'total_employes': Employe.objects.count(),
    }
    return render(request, "db_objects/db-personnels.html", context)

@login_required
def usersEnseignant(request):
    if not request.user.is_superuser:
        # Redirigez les utilisateurs non superutilisateurs vers la page d'accueil
        return redirect("home")
    list_user = CustomUser.objects.all()
    list_etudiant = Etudiant.objects.all()
    list_persAdmin = PersonnelAdministration.objects.all()
    list_enseignant = Enseignant.objects.all()
    context = {
        "utilisateurs": list_user,
        "etudiants": list_etudiant,
        "administrations": list_persAdmin,
        "enseignants": list_enseignant,
        'total_users': CustomUser.objects.count(),
        'total_etudiants': CustomUser.objects.filter(type_utilisateur='etudiant').count(),
        'total_enseignants': CustomUser.objects.filter(type_utilisateur='enseignant').count(),
        'total_personnel': CustomUser.objects.filter(type_utilisateur='personnel_administratif').count(),
        'total_plats': Plat.objects.count(),
        'total_universites': Universite.objects.count(),
        'total_restaurants': Restaurant.objects.count(),
        'total_employes': Employe.objects.count(),
    }
    return render(request, "db_objects/db-enseignants.html", context)

@login_required
def allRestao(request):
    if not request.user.is_superuser:
        # Redirigez les utilisateurs non superutilisateurs vers la page d'accueil
        return redirect("home")
    list_user = CustomUser.objects.all()
    list_etudiant = Etudiant.objects.all()
    list_persAdmin = PersonnelAdministration.objects.all()
    list_enseignant = Enseignant.objects.all()
    list_resto = Restaurant.objects.all()
    context = {
        "utilisateurs": list_user,
        "etudiants": list_etudiant,
        "administrations": list_persAdmin,
        "enseignants": list_enseignant,
        "restaurants": list_resto,
        'total_users': CustomUser.objects.count(),
        'total_etudiants': CustomUser.objects.filter(type_utilisateur='etudiant').count(),
        'total_enseignants': CustomUser.objects.filter(type_utilisateur='enseignant').count(),
        'total_personnel': CustomUser.objects.filter(type_utilisateur='personnel_administratif').count(),
        'total_plats': Plat.objects.count(),
        'total_universites': Universite.objects.count(),
        'total_restaurants': Restaurant.objects.count(),
        'total_employes': Employe.objects.count(),
    }
    return render(request, "db_objects/all-resto.html", context)
#==============AJOUT D UN ARTICLE VIA L ESPACE ADMIN===========
#Nous allons maintenant utiliser les vues fondees sur les classe pour aller rapidement
#cette fonctionutilise d une vue fonder sur les class pour creer , ajouter qqcu a un model
class AddArticle(CreateView):
    model = Plat
    form_class = ArticleForm
    template_name = "add-article.html"
    success_url = reverse_lazy("my-articles")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

#========================End Ajout ==========================

#=================MODIFIER UN ARTICLE =========================
class UpdateArticle(UpdateView):
    model = Plat
    form_class = ArticleForm
    template_name = 'update_form/article-form.html'
    success_url = reverse_lazy("my-articles")
    #success_url = "my-articles"

#==================End ===================

#=========SUPPRIMER UN ARTICLE============
class DeleteArticle(DeleteView):
    model = Plat
    success_url = reverse_lazy("my-articles")
    
    

#=================end==============



class CreateEtudiant(CreateView):
    model = CustomUser
    form_class = EtudiantForm
    template_name = 'add-etudiant.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Cette méthode est appelée lorsqu'un formulaire est validé
        messages.success(self.request, 'Inscription réussie ! Veuillez vous connecter.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Cette méthode est appelée lorsqu'un formulaire n'est pas validé
        messages.error(self.request, "Une erreur s'est produite lors de l'inscription. Veuillez vérifier les informations saisies.")
        return super().form_invalid(form)


class UpdateEtudiant(UpdateView):
    model = CustomUser
    form_class = EtudiantForm
    template_name = 'update_form/etudiant-form.html'
    success_url = reverse_lazy('all-etudiants')  # Remplacez par l'URL souhaitée

    def form_valid(self, form):
        messages.success(self.request, 'Les informations de l\'étudiant ont été mises à jour avec succès.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Une erreur s'est produite lors de la mise à jour des informations de l'étudiant.")
        return super().form_invalid(form)

class DeleteEtudiant(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('all-etudiants')  # Remplacez par l'URL souhaitée

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'L\'étudiant a été supprimé avec succès.')
        return super().delete(request, *args, **kwargs)




# Enseignant Views
class CreateEnseignant(CreateView):
    model = CustomUser
    form_class = EnseignantForm
    template_name = 'add-enseignant.html'
    success_url = reverse_lazy('all-enseignants')

    def form_valid(self, form):
        messages.success(self.request, 'Enseignant créé avec succès.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erreur lors de la création de l'enseignant.")
        return super().form_invalid(form)


class UpdateEnseignant(UpdateView):
    model = CustomUser
    form_class = EnseignantForm
    template_name = 'update_form/enseignant-form.html'
    success_url = reverse_lazy('all-enseignants')

    def form_valid(self, form):
        messages.success(self.request, 'Enseignant mis à jour avec succès.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erreur lors de la mise à jour de l'enseignant.")
        return super().form_invalid(form)


class DeleteEnseignant(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('all-enseignants')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Enseignant supprimé avec succès.')
        return super().delete(request, *args, **kwargs)


# PersonnelAdministration Views
class CreatePersonnelAdmin(CreateView):
    model = CustomUser
    form_class = PersonnelAdminForm
    template_name = 'add-personnel.html'
    success_url = reverse_lazy('all-personnels')

    def form_valid(self, form):
        messages.success(self.request, 'Personnel administratif créé avec succès.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erreur lors de la création du personnel administratif.")
        return super().form_invalid(form)


class UpdatePersonnelAdmin(UpdateView):
    model = CustomUser
    form_class = PersonnelAdminForm
    template_name = 'update_form/personnel-form.html'
    success_url = reverse_lazy('all-personnels')

    def form_valid(self, form):
        messages.success(self.request, 'Personnel administratif mis à jour avec succès.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erreur lors de la mise à jour du personnel administratif.")
        return super().form_invalid(form)


class DeletePersonnelAdmin(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('all-personnels')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Personnel administratif supprimé avec succès.')
        return super().delete(request, *args, **kwargs)