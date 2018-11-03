from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings

from hpp2.utils import unique_customer_id_generator

# Create your models here.
User = settings.AUTH_USER_MODEL

class CustomerProfile(models.Model):
    user         = models.OneToOneField(User)
    customer_id  = models.CharField(max_length=120, blank=True)
    email        = models.EmailField()
    full_name    = models.CharField(max_length=120)
    phone_regex  = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)

    def __str__(self):
        # return str(self.user)
        return self.customer_id




def pre_save_create_customer_id(sender, instance, *args, **kwargs):
    if not instance.customer_id:
        instance.customer_id = unique_customer_id_generator(instance)
    # qs = CustomerProfile.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    # if qs.exists():
    #     qs.update(active=False)


pre_save.connect(pre_save_create_customer_id, sender=CustomerProfile)