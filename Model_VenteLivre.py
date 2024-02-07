from django.db import models
from livre.models import Livre
from accounts.models import CustumerUser
from django.utils.text import slugify


class VenteLivre(models.Model):
    livre         = models.ForeignKey(Livre, on_delete=models.SET_NULL, null=True, max_length=150, verbose_name='Livre :')
    client        = models.ForeignKey(CustumerUser, on_delete=models.SET_NULL, null=True, max_length=150, verbose_name='Client :')
    date_vente    = models.DateField(verbose_name='Date Vente :')
    prix_vente    = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Prix de Vente :')
    sum_payer     = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Somme Payée :')
    reste_a_payer = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Reste à payer :')
    slug          = models.SlugField(max_length=255, unique=True, editable=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.livre.titre} - {self.client.full_name}"

    def save(self, *args, **kwargs):
        if not self.id:
            last_pk = VenteLivre.objects.order_by('pk').last()
            self.slug = slugify(f"{self.livre.titre}-{str(last_pk.pk + 1) if last_pk else '1'}")
        
        if not self.reste_a_payer:
            self.reste_a_payer = self.prix_vente - self.sum_payer

        self.full_clean()
        super().save(*args, **kwargs)
            
    class Meta:
        db_table = 'vente_livre'
        verbose_name = 'vente_livre'
        verbose_name_plural = 'vente_livre'
