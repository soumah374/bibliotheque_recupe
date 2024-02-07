from django.shortcuts import render
from .models import Departement
from .forms import DepartementForm
from django.urls import reverse,reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView


class DepartementCreateView(SuccessMessageMixin,CreateView):
    model = Departement
    form_class = DepartementForm
    success_message = "Département %(libelle_depart)s crée avec succès"
    template_name = 'admin/departement/departement.html'
    success_url = reverse_lazy('departement:departe')
    
    def get_context_data(self, **kwargs):
        context            = super().get_context_data(**kwargs)
        context["departement"] = Departement.objects.order_by('-id')
        context["name"] = "Enregistrer"
        return context
    
class DepartementUpdateView(SuccessMessageMixin,UpdateView):
    model = Departement
    form_class = DepartementForm
    success_message = "Département %(libelle_depart)s Modifié avec succès"
    template_name = 'admin/departement/departement.html'
    success_url = reverse_lazy('departement:departe')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departement"] = Departement.objects.order_by('-id')
        context["name"] = "Modifier"
        return context
    
class DepartementDeleteView(DeleteView):
    model = Departement
    template_name = 'admin/departement/departement.html'
    success_url = reverse_lazy('departement:departe')