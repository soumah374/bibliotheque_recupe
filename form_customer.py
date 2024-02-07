from django import forms
from notification.models import Message,Abonne
from accounts.models import CustumerUser
from django.contrib.auth.forms import UserCreationForm

class CustumerUserForm(UserCreationForm):
    class Meta:
        model = CustumerUser
        fields = ['prenoms','nom','adresse','email','password1','password2']
        widgets = {
            "prenoms":forms.TextInput(attrs={'class': 'form-control'}),
            "nom":forms.TextInput(attrs={'class': 'form-control'}),
            "adresse":forms.TextInput(attrs={'class': 'form-control'}),
            "email":forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'type':'password','class': 'form-control'}),
            'password2': forms.TextInput(attrs={'type':'password','class': 'form-control'}),
        }
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nom_complet','email','tel','objet','detail']
        widgets = {
            'nom_complet':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'type':'email','class':'form-control'}),
            'tel':forms.TextInput(attrs={'class':'form-control'}),
            'objet':forms.TextInput(attrs={'class':'form-control'}),
            'detail':forms.Textarea(attrs={'class':'form-control'}),
        }
        
class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['email_abonne']
        widgets = {
            'email_abonne':forms.TextInput(attrs={'type':'email','class':'form-control bg-transparent text-white', 'placeholder':'Votre Adresse Email'}),
        }