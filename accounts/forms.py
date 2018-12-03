from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from professionals.models import ProfessionalProfile
from addresses.models import Address


User = get_user_model()

SPECIALITY_TYPES = (
    ( 'dental', 'Dental'),
    ( 'vision', 'Vision'),
    ( 'physical', 'Physical'),
    ( 'psychological', 'Psychological'),    
    )


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',) #'full_name',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class GuestForm(forms.Form):
    email    = forms.EmailField()


class LoginForm(forms.Form):
    email    = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


class UserDetailUpdateForm(forms.ModelForm):
    full_name = forms.CharField(label='Name', required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = ['full_name']


class ProfessionalDetailUpdateForm(forms.ModelForm):
    email     = forms.EmailField(label='Email', required=False)
    full_name       = forms.CharField(label='Professional Name', required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = forms.CharField(label='Phone Number', required=False, validators=[phone_regex], max_length=16)
    speciality      = forms.ChoiceField(label='Speciality', required=False, choices=SPECIALITY_TYPES)
    description     = forms.CharField(label='Description', required=False, widget=forms.Textarea())


    class Meta:
        model = ProfessionalProfile
        fields = [
            'full_name',
            'email',
            'phone_number',
            
            'speciality',
            'description',
            # 'professional_address',
        ]


class ProfessionalAddressUpdateForm(forms.ModelForm):
    address_line_1 = forms.CharField(label='Addresses', required=False)
    address_line_2 = forms.CharField(label='Addresses', required=False)
    city           = forms.CharField(label='City', required=False)
    state          = forms.CharField(label='State', required=False)
    country        = forms.CharField(label='Country', required=False)
    postal_code    = forms.CharField(label='Postal Code', required=False)

    class Meta:
        model = Address
        fields = [
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'country',
            'postal_code',
        ]


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',) 

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.active = False # send confirmation email
        if commit:
            user.save()
        return user