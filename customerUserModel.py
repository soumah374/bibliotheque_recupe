from django.db import models
from django.utils.text import slugify
from departement.models import Departement
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Vous devez entrer un email')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(email=email,password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

# Pour le moment j'ai dit que le slug peut être vide
class CustumerUser(AbstractBaseUser):
    ROLE=(
    ('administrateur','Administrateur'),
    ('directeur_general','Directeur Général'),
    ('directeur_adjoint','Directeur Adjoint'),
    ('secretaire','Secrétaire'),
    ('agent','Agent')
    )
    NATURE_CLIENT=(
        ('encadreur','Encadreur'),
        ('etudiant','Etudiant'),
        ('lecteur',"Lecteur/Client")
    )
    SEXE=(
        ('masculin','Masculin'),
        ('feminin','Féminin'),
    )
    NIVEAU=(
        ('licence_1','Licence 1'),
        ('licence_2','Licence 2'),
        ('licence_3','Licence 3'),
        ('licence_4','Licence 4'),
        ('master','Master'),
        ('doctorat','Doctorat'),
    )
    nom           = models.CharField(max_length=150, blank=True, null=True, verbose_name='Nom* :')
    prenoms       = models.CharField(max_length=150, blank=True, null=True, verbose_name='Prénoms :')
    slug          = models.SlugField(max_length=255, unique=True, editable=False ,blank=True, null=True,)
    adresse       = models.CharField(max_length=150, blank=True, null=True, verbose_name='Adresse* :')
    email         = models.EmailField(max_length=255, unique=True, blank=False, verbose_name='Email ')
    tel           = models.CharField(max_length=150, blank=True, null=True, verbose_name='Téléphone*')
    profession    = models.CharField(max_length=150,blank=True,null=True,verbose_name='Profession*')
    sexe          = models.CharField(max_length=150,choices=SEXE,blank=True,null=True,verbose_name='Sexe*')
    nature_client = models.CharField(max_length=150, blank=True, null=True,choices=NATURE_CLIENT, verbose_name='Nature Client*')
    departement   = models.ForeignKey(Departement,on_delete=models.SET_NULL, max_length=150,blank=True,null=True,verbose_name='Département/Spécialisation*')
    niveau        = models.CharField(max_length=150, blank=True, null=True,choices=NIVEAU, verbose_name='Niveau*')
    matricule     = models.CharField(max_length=150,blank=True,null=True,verbose_name='Matricule*')
    role          = models.CharField(max_length=150, blank=True, null=True,choices=ROLE, verbose_name='Rôle*')
    photo         = models.ImageField(upload_to='accounts', blank=True, null=True, verbose_name='Photo*')
    pays          = models.CharField(max_length=150, blank=True, null=True, verbose_name='Pays*')
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    is_admin      = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            last_pk = CustumerUser.objects.order_by('pk').last()
            self.slug = slugify((self.nom) + (self.prenoms)) + '-' + str(last_pk.pk + 1) if last_pk else '1'
        super(CustumerUser, self).save(*args, **kwargs)
    
    # def save(self, *args, **kwargs):
    #     id = CustumerUser.objects.count()+1
    #     if not self.slug:
    #         self.slug = slugify((self.nom)+(self.prenoms))+'-'+str(id)
    #     super().save(*args, **kwargs)
    
    
    USERNAME_FIELD = "email"
    objects = MyUserManager()
            
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    