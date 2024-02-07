import django.contrib
from django.shortcuts import render
from configuration.models import Configuration
from configuration.forms import ConfigurationForm
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
    param = Configuration.objects.all().last()
    id = param.id
    if id == None: id=0
    init_param = {}
    init_param['nomentreprise'] = param.nomentreprise
    init_param['abreviation'] = param.abreviation
    init_param['slogan'] = param.slogan
    init_param['directeur'] = param.directeur
    init_param['adresse'] = param.adresse
    init_param['telephone'] = param.telephone
    init_param['email'] = param.email
    init_param['logo'] = param.logo
    form = ConfigurationForm(initial=init_param)
    if request.method == 'POST':
        nomentreprise = request.POST.get('nomentreprise')
        abreviation = request.POST.get('abreviation')
        slogan = request.POST.get('slogan')
        directeur = request.POST.get('directeur')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        logo = request.FILES.get('logo')
        if nomentreprise == "":
            ConfigurationForm.objects.create(nomentreprise=nomentreprise,abreviation=abreviation,slogan=slogan,directeur=directeur,adresse=adresse,telephone=telephone,email=email,logo=logo)
            messages.success(request, "Connfiguration ajoutée  avec succès")
        else:
            params = Configuration.objects.all().last()
            params.nomentreprise = request.POST.get('nomentreprise')
            params.abreviation = request.POST.get('abreviation')
            params.slogan = request.POST.get('slogan')
            params.directeur = request.POST.get('directeur')
            params.adresse = request.POST.get('adresse')
            params.telephone = request.POST.get('telephone')
            params.email = request.POST.get('email')
            params.logo = request.FILES.get('logo')
            params.save()         
            messages.success(request, "configuration modifiée avec succès")
        return HttpResponseRedirect(request.path)
    return render(request, "admin/configuration/index.html",{'form':form})