from django.conf.urls import url

from .views import (
        AccountHomeView,
        UserDetailUpdateView,
        professional_profile_form_view,
        ProfessionalAccountHomeView,

        )

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    url(r'^professional/register', professional_profile_form_view, name='register'),
    # url(r'^professional/login', , name='login'),
    url(r'^professional/home', ProfessionalAccountHomeView.as_view(), name='pro_home'),
]
