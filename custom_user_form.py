from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import CustumerUser

class CustumerUserForm(UserCreationForm):
    class Meta:
        model = CustumerUser
        fields = ['prenoms','nom','adresse','email','tel','profession','sexe','nature_client','departement','niveau','matricule','role','photo','pays','password1','password2']
        widgets = {
            "prenoms":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "nom":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "adresse":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "email":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "tel":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            'profession': forms.TextInput(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'sexe': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'nature_client': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'departement': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'niveau': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'role': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'pays': forms.TextInput(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'password1': forms.TextInput(attrs={'type':'password','class': 'form-control form-control-rounded choices__input'}),
            'password2': forms.TextInput(attrs={'type':'password','class': 'form-control form-control-rounded choices__input'}),
        }
        

class ChangeCustumerUserForm(UserChangeForm):
     class Meta:
        model = CustumerUser
        fields = ['prenoms','nom','adresse','email','tel','profession','sexe','nature_client','departement','niveau','matricule','role','photo','pays']
        widgets = {
            "prenoms":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "nom":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "adresse":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "email":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            "tel":forms.TextInput(attrs={'class': 'form-control form-control-rounded'}),
            'profession': forms.TextInput(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'sexe': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'nature_client': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'departement': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'niveau': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'role': forms.Select(attrs={'class': 'form-control form-control-rounded choices__input'}),
            'pays': forms.TextInput(attrs={'class': 'form-control form-control-rounded choices__input'}),
        }
        
        
# class ChangePasswordForm(forms.Form):
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))