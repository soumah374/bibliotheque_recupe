from django.db import models
from django.utils.text import slugify
# from django.contrib.auth import  get_user_model

# User = get_user_model()

class DepartementManager(models.Manager):
    def create_departement(self, libelle_depart):
        last_pk = self.order_by('pk').last()
        slug    = slugify(libelle_depart) + '-' + str(last_pk.pk + 1) if last_pk else '1'
        return self.create(libelle_depart=libelle_depart, slug=slug)

class Departement(models.Model):
    libelle_depart = models.CharField(max_length=150, unique=True, verbose_name='Département :')
    slug           = models.SlugField(max_length=255, unique=True, editable=False)
    # user           = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    objects = DepartementManager()

    def __str__(self):
        return self.libelle_depart
    
    class Meta:
        db_table = 'departement'
        verbose_name = 'departement'
        verbose_name_plural = 'departements'
