from typing import Any
from django.shortcuts import render,redirect
from .models import Emprunt
from .forms import EmpruntForm
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView


class EmpruntCreateView(CreateView):
    model = Emprunt
    form_class = EmpruntForm
    template_name = 'admin/emprunt/create.html'
    success_url = reverse_lazy('emprunt:index')
    
class EmpruntListView(ListView):
    model = Emprunt
    context_object_name = 'emprunts'
    template_name = 'admin/emprunt/index.html'
    
def Update_statut(request):
    if request.method=='POST':
        em_state = request.POST.get('statut')
        id_statut = request.POST.get('id_statut')
        objet = Emprunt.objects.get(id=id_statut,statut=em_state)
        if objet.statut == 0:
            objet.statut = True
            objet.save()
        else :
            objet.statut = False
            objet.save()
    return redirect('emprunt:index')
    
class EmpruntUpdateView(UpdateView):
    model = Emprunt
    form_class = EmpruntForm
    template_name = 'admin/emprunt/update.html'
    context_object_name = 'emprunts'
    success_url = reverse_lazy('emprunt:index')
    
class EmpruntDetailView(DetailView):
    model = Emprunt
    context_object_name = 'emprunts'
    template_name = 'admin/emprunt/detail.html'
    
class EmpruntDeleteView(DeleteView):
    model = Emprunt
    template_name = 'admin/emprunt/index.html'
    success_url = reverse_lazy('emprunt:index')