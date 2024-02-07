from django.db import models
from django.utils.text import slugify
from livre.models import Livre
from accounts.models import CustumerUser
# from django.contrib.auth import get_user_model

# User = get_user_model()

class Emprunt(models.Model):
    ETAT_LIVRE=(
    ('bon','Bon'),
    ('degrader','Dégradé'),
    ('mauvais','Mauvais')
    )
    categorie = models.ForeignKey(Livre,on_delete=models.SET_NULL, max_length=150,null=True,verbose_name='Livre :')
    client = models.ForeignKey(CustumerUser,on_delete=models.SET_NULL,max_length=150,null=True,verbose_name='Client :')
    date_emprunt = models.DateField(verbose_name='Date Emprunt :')
    date_retour = models.DateField(verbose_name='Date Retour :')
    slug = models.SlugField(max_length=255,unique=True,editable=False)
    etat_livre= models.CharField(max_length=150,choices=ETAT_LIVRE,blank=True,null=True,verbose_name="Etat du Livre à L'emprunt")
    # user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank= True)
    statut = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            last_pk = Emprunt.objects.order_by('pk').last()
            self.slug = slugify((self.categorie) + (self.categorie)) + '-' + str(last_pk.pk + 1) if last_pk else '1'
        super().save(*args, **kwargs)
            
    class Meta:
        db_table = 'emprunt'
        verbose_name = 'emprunt'
        verbose_name_plural = 'emprunts'