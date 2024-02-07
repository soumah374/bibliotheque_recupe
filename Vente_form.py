from django import forms
from .models import VenteLivre

class VenteLivreForm(forms.ModelForm):
    class Meta:
        model = VenteLivre
        fields = ['livre','client','date_vente','prix_vente','sum_payer']
        widgets = {
            "sum_payer":forms.TextInput(attrs={"type":"number",'class': 'form-control form-control-rounded'}),
            "prix_vente":forms.TextInput(attrs={"type":"number",'class': 'form-control form-control-rounded'}),
            "date_vente":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            'livre': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'client': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
        }
        