from django import forms
from .models import Emprunt

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['categorie','client','date_emprunt','date_retour','etat_livre']
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'client': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            "date_emprunt":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            "date_retour":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            'etat_livre': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
        }
        