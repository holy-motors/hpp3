from django.db import models

from billing.models import BillingProfile

# Create your models here.
ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('professional', 'Professional'),
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, null=True)
    address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES, default='billing')
    address_line_1  = models.CharField(max_length=120, null=True)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120, null=True)
    country         = models.CharField(max_length=120, default='USA')
    state           = models.CharField(max_length=120, null=True)
    postal_code     = models.CharField(max_length=120, null=True)

    def __str__(self):
        return str(self.billing_profile)


    def get_address(self):
        return "{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
                line1 = self.address_line_1,
                line2 = self.address_line_2 or "",
                city = self.city,
                state = self.state,
                postal= self.postal_code,
                country = self.country
            )