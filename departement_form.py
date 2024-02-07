from django import forms
from .models import Departement

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['libelle_depart']
        widgets = {
            "libelle_depart":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
        }