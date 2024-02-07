from django import forms
from .models import Actualite

class ActualiteForm(forms.ModelForm):
    class Meta:
        model = Actualite
        fields = ['type_pub','titre','sous_titre','date_pub','lieu','prenoms','nom','profession','photo','detail']
        widgets = {
            'type_pub': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            "titre":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "sous_titre":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "date_pub":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            "lieu":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "prenoms":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "nom":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "profession":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "detail":forms.Textarea(attrs={'class': 'form-control form-control-rounded'}),
        }
        