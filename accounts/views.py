from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views.generic import CreateView, FormView, View, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.utils.http import is_safe_url

from addresses.forms import AddressForm
from professionals.forms import ProfessionalProfileForm

from billing.models import BillingProfile
# from professionals.views import professional_profile_form_view

from .forms import LoginForm, RegisterForm, GuestForm, UserDetailChangeForm
from .models import GuestEmail


# Create your views here.
# ???
# class ProfessionalProfileActivationView(FormMixin, View):



class ProfessionalAccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/professional_home.html'
    def get_object(self):
        return self.request.user


#LoginRequiredMixin,
class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/home.html'
    def get_object(self):
        return self.request.user

#class ProfessionalProfileFormView(View):
    ## Two goal - 1. is_pro = True, 2. save the ProfessinalProfile
    # user = self.request.user



@login_required
def professional_profile_form_view(request):
    profile_form = ProfessionalProfileForm(request.POST or None)
    address_form = AddressForm(request.POST or None)
    context = {
        "profile_form": profile_form,
        "address_form": address_form
    }

    user = request.user
    if user.is_pro:
        redirect("account:pro_home")

    else:
        if address_form.is_valid():
            print(request.POST)
            instance = address_form.save(commit=False)
            billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
            if billing_profile is not None:
                address_type = request.POST.get('address_type', 'professional')
                instance.billing_profile = billing_profile
                instance.address_type = address_type
                instance.save()
                request.session[address_type + "_address_id"] = instance.id
                request.session["address_id"] = instance.id
                print(address_type + "_address_id")
                
            else:
                print("Error here")
                

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            # Assign User ID to profile
            # user = request.user
            profile.user = user
            print(instance)

            profile.professional_address = instance
            profile.save()

            user.is_pro = True
            user.save()

            redirect("account:pro_home")

    return render(request, "accounts/form.html", context)


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email       = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")

    
class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
              #  del request.session['guest_email_id']
              pass
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'


class UserDetailUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserDetailChangeForm
    template_name = 'accounts/detail-update-view.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Change Your Account Details'
        return context

    def get_success_url(self):
        return reverse("account:home")
