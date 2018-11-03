from django.contrib import admin
from .models import ProfessionalProfile

# Register your models here.
class ProfessionalProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', '__str__', 'slug']
    class Meta:
        model = ProfessionalProfile


admin.site.register(ProfessionalProfile, ProfessionalProfileAdmin)