from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Auteur
from .forms import AuteurForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView


class AuteurCreateView(SuccessMessageMixin,CreateView):
    model = Auteur
    form_class = AuteurForm
    success_message = "Auteur %(prenoms)s %(nom)s créée avec succès"
    template_name = 'admin/auteur/create.html'
    success_url = reverse_lazy('auteur:index')
    
class AuteurListView(ListView):
    model = Auteur
    context_object_name = 'auteur'
    template_name = 'admin/auteur/index.html'

class AuteurUpdateView(SuccessMessageMixin,UpdateView):
    model          = Auteur
    form_class     = AuteurForm
    template_name  = "admin/auteur/update.html"
    context_object_name = "auteur"
    success_url    = reverse_lazy("auteur:index")
    success_message = "Auteur %(prenoms)s %(nom)s Modifié avec succès"
    
class AuteurDetailView(DetailView):
    model = Auteur
    context_object_name = 'auteur'
    template_name = 'admin/auteur/detail.html'
    
class AuteurDeleteView(DeleteView):
    model = Auteur
    template_name = 'admin/auteur/index.html'
    success_url = reverse_lazy('auteur:index')