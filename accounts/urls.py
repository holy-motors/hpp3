from django.conf.urls import url

from .views import (
        AccountHomeView,
        UserDetailUpdateView,
        professional_profile_form_view,
        ProfessionalAccountHomeView,
        ProfessionalDetailUpdateView,
        TestView,

        )

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    url(r'^professional/register', professional_profile_form_view, name='register'),
    # url(r'^professional/login', , name='login'),
    url(r'^professional/home', ProfessionalAccountHomeView.as_view(), name='pro_home'),
    url(r'^professional/details/', ProfessionalDetailUpdateView.as_view(), name='pro-update'),
    url(r'^professional/test', TestView.as_view(), name='test-update'),
 #   url(r'^professional/search', TestView.as_view(), name='cus-search'),

]
