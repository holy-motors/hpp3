from django import forms

from .models import ProfessionalProfile


class ProfessionalProfileForm(forms.ModelForm):
	class Meta:
		model = ProfessionalProfile
		fields = [
			'full_name',
			'phone_number',
			
			'speciality',
			'description',
			# 'professional_address',
		]