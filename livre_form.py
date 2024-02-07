from django import forms
from .models import Livre

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['categorie','titre','sous_titre','resume','auteur','langue','annee','distinction','nbre_exemplaire','prix_vente','photo_livre','fichier_livre','num_livre']
        widgets = {
            "titre":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "sous_titre":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "langue":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "annee":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            "date_deces":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            "nbre_exemplaire":forms.TextInput(attrs={"type":"number",'class': 'form-control form-control-rounded'}),
            "num_livre":forms.TextInput(attrs={"type":"number",'class': 'form-control form-control-rounded'}),
            "distinction":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "resume":forms.Textarea(attrs={'class': 'form-control form-control-rounded'}),
            "prix_vente":forms.TextInput(attrs={"type":"number",'class': 'form-control form-control-rounded'}),
            'categorie': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'auteur': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
        }
        