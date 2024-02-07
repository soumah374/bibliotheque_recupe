from django import forms
from .models import Message,Abonne

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nom_complet','email','tel','objet','detail']
        widgets = {
            'nom_complet':forms.TextInput(attrs={'class':'form-control form-control-rounded'}),
            'email':forms.TextInput(attrs={'type':'email','class':'form-control form-control-rounded'}),
            'tel':forms.TextInput(attrs={'class':'form-control form-control-rounded'}),
            'objet':forms.TextInput(attrs={'class':'form-control form-control-rounded'}),
            'detail':forms.Textarea(attrs={'class':'form-control form-control-rounded'}),
        }
        
class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['email_abonne']
        widgets = {
            'email_abonne':forms.TextInput(attrs={'type':'email','class':'form-control form-control-rounded'}),
        }