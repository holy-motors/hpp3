from django.conf.urls import url

from .views import (
        AccountHomeView,
        professional_profile_form_view,
        ProfessionalAccountHomeView,
        )

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^professional/register', professional_profile_form_view, name='register'),
    url(r'^professional/home', ProfessionalAccountHomeView, name='pro_home'),
]
