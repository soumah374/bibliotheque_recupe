from django.shortcuts import redirect
from .models import Message,Abonne
from django.views.generic import ListView,DetailView



    
class MessageListView(ListView):
    model = Message
    context_object_name = 'notif_messages'
    template_name = 'admin/notification/index_message.html'

def Update_statut(request):
    if request.method=='POST':
        s = request.POST.get('statut')
        id_s = request.POST.get('id_statut')
        objet = Message.objects.get(id=id_s,statut=s)
        if s == 'False':
            objet.statut = True
            objet.save()
        else :
            objet.statut = False
            objet.save()
    return redirect('message-index')
    
class MessageDetailView(DetailView):
    model = Message
    context_object_name = 'notif_messages'
    template_name = 'admin/notification/detail_message.html'
    
    
class AbonneListView(ListView):
    model = Abonne
    context_object_name = 'notif_abonnes'
    template_name = 'admin/notification/index_abonne.html'
    

class AbonneDetailView(DetailView):
    model = Abonne
    context_object_name = 'notif_abonnes'
    template_name = 'admin/notification/detail_abonne.html'
    