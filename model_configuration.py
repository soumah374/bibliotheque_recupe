from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Configuration(models.Model):
    nomentreprise = models.CharField(max_length=100, unique=True, verbose_name="Nom Entreprise")
    abreviation = models.CharField(max_length=100)
    slogan = models.CharField(max_length=255)
    directeur = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.BigIntegerField(unique=True, verbose_name="Téléphone")
    email =  models.EmailField(max_length=50, unique=True,null=True,blank=True)
    logo = models.ImageField(upload_to="entreprise/logo", null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True,blank= True)
    
    def __str__(self):
        return self.nomentreprise
    
    class Meta:
        db_table = "configuration"
        verbose_name = 'configuration' 
        verbose_name_plural = 'configurations'
    