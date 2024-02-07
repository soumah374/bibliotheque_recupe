from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Actualite
from .forms import ActualiteForm
from django.urls import reverse,reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView

# SuccessMessageMixin,
class ActualiteCreateView(CreateView):
    model = Actualite
    form_class = ActualiteForm
    template_name = 'admin/actualite/create.html'
    success_url = reverse_lazy('actualite:index')
    # success_message = "Actualité créée avec succès"
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            messages.success(self.request, f"Actualité {self.request.POST.get('titre')} créé avec succès !")
        return super().form_valid(form)
    
class ActualiteListView(ListView):
    model = Actualite
    context_object_name = 'actualite'
    template_name = 'admin/actualite/index.html'
    
def update_publiciter(request):
    
    if request.method=='POST':
        p_state = request.POST.get('publier')
        p_id = request.POST.get('idpublier')
        objet = Actualite.objects.get(id=p_id,publier=p_state)
        
        if p_state == 'False':
            objet.publier = True
            objet.save()
        else :
            objet.publier = False
            objet.save()
            
    return redirect('actualite:index')
    
class ActualiteUpdateView(SuccessMessageMixin,UpdateView):
    model = Actualite
    form_class = ActualiteForm
    template_name = 'admin/actualite/update.html'
    context_object_name = 'actualite'
    success_url = reverse_lazy('actualite:index')
    success_message = "Actualité Modifiée avec succès"
    
class ActualiteDetailView(DetailView):
    model = Actualite
    context_object_name = 'actualite'
    template_name = 'admin/actualite/detail.html'
    
class ActualiteDeleteView(DeleteView):
    model = Actualite
    template_name = 'admin/actualite/index.html'
    success_url = reverse_lazy('actualite:index')