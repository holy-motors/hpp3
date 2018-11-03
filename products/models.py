import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from hpp2.utils import unique_slug_generator
# Create your models here.

PLAN_TYPES = (
    ( 'dental', 'Dental'),
    ( 'vision', 'Vision'),
    ( 'physical', 'Physical'),
    ( 'psychological', 'Psychological'),    
    )

# PLAN_TYPES = (
#     ( 1, 'Dental'),
#     ( 2, 'Vision'),
#     ( 3, 'Physical'),
#     ( 4, 'Psychological'),    
#     )


# PLAN_PERIOD = (
#     ( 1, '1 year'),
#     ( 2, '2 years'),
#     ( 3, '3 years'),
#     ( 4, '4 years'),    
#     )

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    # def featured(self):
    #     return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    """docstring for ProductManager"""
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    # def featured(self): #Product.objects.featured() 
    #     return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    # def search(self, query):
    #     return self.get_queryset().active().search(query)


class Product(models.Model):
    plan          = models.CharField(max_length=120, choices=PLAN_TYPES, default='dental')
    # plan = models.IntegerField(choices=PLAN_TYPES, default=1)
    slug          = models.SlugField(blank=True, unique=True)
    description   = models.TextField()
    price         = models.DecimalField(max_digits=10, decimal_places=2, default=120)
    # period = models.IntegerField(choices=PLAN_PERIOD, default=1)
    active        = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
    #return "/products/{slug}/".format(slug=self.slug)
        return reverse("home:detail", kwargs={"slug": self.slug})

    def __str__(self):
        # return str(self.plan)
        return self.plan

    def __unicode__(self):
        # return str(self.plan)
        return self.plan

    @property
    def name(self):
        return self.plan


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)







