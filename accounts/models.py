from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
    )
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    # full_name   = models.CharField(max_length=255, blank=True, null=True)
    active      = models.BooleanField(default=True) # can login
    is_pro      = models.BooleanField(default=False)
    staff       = models.BooleanField(default=False) # staff user non superuser
    admin       = models.BooleanField(default=False) # superuser 
    timestamp   = models.DateTimeField(auto_now_add=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# class ProfessionalProfileQuerySet(models.query.QuerySet):
#     def confirmable(self):
#         #now = timezone.now()
#         #start_range = now - timedelta(days=DEFAULT_ACTIVATION_DAYS)
#         # does my object have a timestamp in here
#         #end_range = now
#         return self.filter(
#                 activated = False
#                 #forced_expired = False
#                 )

#               # ).filter(
#               #   timestamp__gt=start_range,
#               #   timestamp__lte=end_range
#               # )


# class ProfessionalProfileActivationManager(models.Manager):
#     def get_queryset(self):
#         return ProfessionalProfileQuerySet(self.model, using=self._db)

#     def confirmable(self):
#         return self.get_queryset().confirmable()


# class ProfessionalProfileActivation(models.Model):
#     user            = models.ForeignKey(User)
#     email           = models.EmailField()
#     activated       = models.BooleanField(default=False)
#     timestamp       = models.DateTimeField(auto_now_add=True)
#     update          = models.DateTimeField(auto_now=True)

#     objects = ProfessionalProfileActivationManager()

#     def __str__(self):
#         return self.email

#     def can_activate(self):
#         qs = EmailActivation.objects.filter(pk=self.pk).confirmable() # 1 object
#         if qs.exists():
#             return True
#         return False

#     def activate(self):
#         if self.can_activate():
#             # pre activation user signal
#             user = self.user
#             user.is_active = True
#             user.save()
#             # post activation signal for user
#             self.activated = True
#             self.save()
#             return True
#         return False
