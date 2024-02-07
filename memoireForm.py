from django import forms
from .models import Memoire

class MemoireForm(forms.ModelForm):
    class Meta:
        model = Memoire
        fields = ['titre','sous_titre','nature_memorant','annee','client','resumer']
        widgets = {
            "titre":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "sous_titre":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "resumer":forms.Textarea(attrs={'class': 'form-control form-control-rounded'}),
            "annee":forms.TextInput(attrs={"type":"date",'class': 'form-control form-control-rounded'}),
            'client': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            "nature_memorant":forms.Select(attrs={'class': 'form-control form-control-rounded'}),
        }
        