from django.conf import settings
from django.core.validators import RegexValidator

from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from addresses.models import Address

from hpp2.utils import unique_slug_generator

# Create your models here.
User = settings.AUTH_USER_MODEL


# SPECIALITY_TYPES = (
#     ( 1, 'Dental'),
#     ( 2, 'Vision'),
#     ( 3, 'Physical'),
#     ( 4, 'Psychological'),    
#     )

SPECIALITY_TYPES = (
    ( 'dental', 'Dental'),
    ( 'vision', 'Vision'),
    ( 'physical', 'Physical'),
    ( 'psychological', 'Psychological'),    
    )


class ProfessionalProfileQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (
            Q(address__address_line_1 = query) |
            Q(address__city = query) |
            Q(address__country = query) |
            Q(address__state = query) |
            Q(address__postal_code = query)
            )
        return self.filter(lookups).distinct()


class ProfessionalProfileManager(models.Manager):
    def get_queryset(self):
        return ProfessionalProfileQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        lookups = (Q(address__country__icontains=query) | 
          Q(address__city__icontains=query) |
          Q(description__icontains=query) |
          Q(full_name__icontains=query) 
          )
        return self.filter(lookups).distinct()


class ProfessionalProfile(models.Model):
    user            = models.OneToOneField(User)
    email           = models.EmailField()
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = models.CharField(validators=[phone_regex], max_length=16) # Require it in  # validators should be a list
    full_name       = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True)#, unique=True) 
    # phone_number = models.CharField(max_length=16)
    # speciality   = models.IntegerField(choices=SPECIALITY_TYPES, default=1)
    speciality      = models.CharField(max_length=120, choices=SPECIALITY_TYPES, default='dental')
    description     = models.TextField(blank=True)
    active          = models.BooleanField(default=True)
    update          = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    # Address
    # address_line_1  = models.CharField(max_length=120, null=True)
    # address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    # city            = models.CharField(max_length=120, null=True)
    # country         = models.CharField(max_length=120, default='Canada')
    # state           = models.CharField(max_length=120, null=True)
    # postal_code     = models.CharField(max_length=120, null=True)
    address = models.OneToOneField(Address, null=True)

    objects = ProfessionalProfileManager()

    def get_absolute_url(self):
        return reverse("professionals:detail", kwargs={"slug":self.slug})


    def __str__(self):
        return str(self.user)



def professional_profile_pre_save_receiver(sender, instance, *args, **kwargs):
    if (not instance.slug) or instance.slug=="register":
        instance.slug = unique_slug_generator(instance, filed="full_name")


pre_save.connect(professional_profile_pre_save_receiver, sender=ProfessionalProfile)



