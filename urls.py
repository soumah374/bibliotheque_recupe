"""
URL configuration for bibliotheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import IndexTemplateView,ContacteTemplateView,InscriptionTemplateView,ProposTemplateView,DashboardTemplateView,CategorieLivre,CategorieLivre_liste

urlpatterns = [
    path('admin/', admin.site.urls),
    ################### LES VUES DU SITE ####################################
    
    path('', IndexTemplateView.as_view(), name='index'),
    path('contacte/', ContacteTemplateView.as_view(), name='contacte'),
    path('propos/', ProposTemplateView.as_view(), name='propos'),
    path('inscription/', InscriptionTemplateView.as_view(), name='inscription'),
    path('categories_livre/<int:pk>/',CategorieLivre, name='categorie_livre'),
    path('categories_livre_liste/<int:pk>/',CategorieLivre_liste, name='categorie_livre_liste'),
    
    ################### LES VUES DU BACK_OFFICE #############################
    
    path('accounts/dashboard', DashboardTemplateView.as_view(), name='dashboard'),
    path('connexion/', auth_views.LoginView.as_view(), name='connexion'),
    path('deconnexion/',auth_views.LogoutView.as_view(),name="deconnexion"),
    path('accouts/',include("django.contrib.auth.urls")),
    path('accounts/',include("accounts.urls")),
    path('departement/',include("departement.urls")),
    path('actualite/',include("actualite.urls")),
    path('auteur/',include("auteur.urls")),
    path('categorie/',include("categorie.urls")),
    path('livre/',include("livre.urls")),
    path('configuration/',include("configuration.urls")),
    path('vente_livre/',include("vente_livre.urls")),
    path('memoire/',include("memoire.urls")),
    path('emprunt/',include("emprunt.urls")),
    path('notification/',include("notification.urls")),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
