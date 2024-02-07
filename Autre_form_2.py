from django import forms
from .models import Auteur

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom','prenoms','sexe','nationalite','date_naiss','date_deces','pays']
        widgets = {
            "nom":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "prenoms":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "nationalite":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "pays":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "date_naiss":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            "date_deces":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            'sexe': forms.Select(attrs={'class': 'form-control choices__input','class': 'form-control form-control-rounded'}),
        }
        