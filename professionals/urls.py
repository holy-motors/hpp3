from django.conf.urls import url


from professionals.views import (
    ProfessionalProfileListView,
    ProfessionalProfileDetailSlugView, 
    #professional_profile_form_view,
    )


urlpatterns = [
    url(r'^$', ProfessionalProfileListView.as_view(), name='list'),
    #url(r'^register/', professional_profile_form_view, name='register'),
    url(r'^(?P<slug>[\w-]+)/$', ProfessionalProfileDetailSlugView.as_view(), name='detail'),

    ]
