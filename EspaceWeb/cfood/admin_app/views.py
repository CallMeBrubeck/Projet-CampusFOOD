from django.shortcuts import render, redirect
from cfoodapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from cfoodapp.forms import *

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
    return render(request, "db.html")


#fonction pour avoir acces aux article dans notre admin
@login_required
def user_articles(request):
    # Vérifiez si l'utilisateur est superutilisateur
    if not request.user.is_superuser:
        # Redirigez les utilisateurs non superutilisateurs vers la page d'accueil
        return redirect("home")

    # Récupérez tous les articles de la base de données
    list_articles = Plat.objects.all()
    return render(request, "my-articles.html", {"list_articles": list_articles})
""" def user_articles(request):
    #si l administrateur n est pas connecter et quon essay d acceder a la page via le liens, on va lui refuser l acces
    if not request.user.is_authenticated:
        return redirect("home")
    #on va faire un filtre pour affihcer les articles dun utilisaturs
    list_articles = Plat.objects.filter(user=request.user)
    return render(request, "my-articles.html", {"list_articles": list_articles}) """


#==============AJOUT D UN ARTICLE VIA L ESPACE ADMIN===========
#Nous allons maintenant utiliser les vues fondees sur les classe pour aller rapidement
#cette fonctionutilise d une vue fonder sur les class pour creer , ajouter qqcu a un model
class AddArticle(CreateView):
    model = Plat
    form_class = ArticleForm
    template_name = "add-article.html" #pour le template d ajout de l article
    success_url = "my-articles" #pour le lient ou on doit me rediriger si l article est bien ajouter

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
        

#========================End Ajout ==========================

#=================MODIFIER UN ARTICLE =========================
class UpdateArticle(UpdateView):
    model = Plat
    form_class = ArticleForm
    template_name = 'app_admin/article-form.html'
    #success_url = "my-articles"

#==================End ===================

#=========SUPPRIMER UN ARTICLE============
class DeleteArticle(DeleteView):
    model = Plat
    success_url = "/my-admin/my-articles"
    
    

#=================end==============
