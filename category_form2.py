from django import forms
from .models import Categorie

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['libelle_categ']
        widgets = {
            "libelle_categ":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
        }
        