from django.db import models
from accounts.models import CustumerUser
from django.utils.text import slugify
# from django.contrib.auth import get_user_model

# User = get_user_model()


class Memoire(models.Model):
    NATURE_MEMO=(
    ('etudiant','Etudiant'),
    ('encadreur','Encadreur')
    )
    titre          = models.CharField(max_length=150,verbose_name='Titre :')
    sous_titre     = models.CharField(max_length=150,verbose_name='Sous Titre :')
    resumer        = models.TextField(max_length=150,verbose_name='Resumé :')
    annee          = models.DateField(verbose_name='Année')
    client         = models.ForeignKey(CustumerUser,on_delete=models.SET_NULL,null=True,verbose_name='Utilisateur')
    nature_memorant= models.CharField(max_length=150,choices=NATURE_MEMO,blank=True,null=True,verbose_name='Nature')
    # user           = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=255,unique=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            last_pk = Memoire.objects.order_by('pk').last()
            self.slug = slugify((self.titre) + (self.sous_titre)) + '-' + str(last_pk.pk + 1) if last_pk else '1'
        super().save(*args, **kwargs)
            
    class Meta:
        db_table = 'memoire'
        verbose_name = 'memoire'
        verbose_name_plural = 'memoires'