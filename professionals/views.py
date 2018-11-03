from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from addresses.forms import AddressForm
from billing.models import BillingProfile
from .forms import ProfessionalProfileForm
from .models import ProfessionalProfile

# Create your views here.
class ProfessionalProfileListView(ListView):
    queryset = ProfessionalProfile.objects.all()
    template_name = 'professionals/list.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProfessionalProfileListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class ProfessionalProfileDetailSlugView(DetailView):
    queryset = ProfessionalProfile.objects.all()
    template_name = "professionals/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfessionalProfileDetailSlugView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = ProfessionalProfile.objects.get(slug=slug, active=True)
        except ProfessionalProfile.DoesNotExist:
            raise Http404("Not found..")
        except ProfessionalProfile.MultipleObjectsReturned:
            qs = ProfessionalProfile.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance



## Move to account views
# def professional_profile_form_view(request):
#     form = ProfessionalProfileForm(request.POST or None)
#     address_form = AddressForm(request.POST or None)
#     context = {
#         "form": form,
#         "address_form": address_form
#     }

#     if address_form.is_valid():
#         print(request.POST)
#         instance = address_form.save(commit=False)
#         billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
#         if billing_profile is not None:
#             address_type = request.POST.get('address_type', 'professional')
#             instance.billing_profile = billing_profile
#             instance.address_type = address_type
#             instance.save()
#             request.session[address_type + "_address_id"] = instance.id
#             request.session["address_id"] = instance.id
#             print(address_type + "_address_id")
            
#         else:
#             print("Error here")
#             return redirect("home")

#     if form.is_valid():
#         profile = form.save(commit=False)
#         # Assign User ID to profile
#         profile.user = request.user
#         print(instance)

#         profile.professional_address = instance
#         profile.save()

#     return render(request, "professionals/form.html", context)