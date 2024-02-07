from django.db import models
from django.contrib.auth import  get_user_model
from django.utils.text import slugify

User = get_user_model()

class Auteur(models.Model):
    SEXE=(
    ('masculin','Masculin'),
    ('feminin','Féminin'),
    )
    nom         = models.CharField(max_length=150,verbose_name='Nom :')
    prenoms     = models.CharField(max_length=150,verbose_name='Prénoms :')
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    slug        = models.SlugField(max_length=255,unique=True,editable=False)
    sexe        = models.CharField(max_length=150,choices=SEXE,blank=True,null=True,verbose_name='Sexe*')
    nationalite = models.CharField(max_length=150,verbose_name='Nationalité :')
    date_naiss  = models.DateField(verbose_name='Date Naissance :')
    date_deces  = models.DateField(blank=True,null=True,verbose_name='Date Décès :')
    pays        = models.CharField(max_length=150,verbose_name='Pays :')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    @property
    def full_name(self):
        return f"{self.prenoms} {self.nom}"
    
    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            last_pk = Auteur.objects.order_by('pk').last()
            self.slug = slugify((self.nom) + (self.prenoms)) + '-' + str(last_pk.pk + 1) if last_pk else '1'
        super().save(*args, **kwargs)
    
    
    class Meta:
        db_table = 'auteur'
        verbose_name = 'auteur'
        verbose_name_plural = 'auteurs'