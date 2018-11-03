"""hpp2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView


from accounts.views import LoginView, RegisterView
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from carts.views import cart_detail_api_view
# from professionals.views import professional_profile_form_view

from .views import about_page, contact_page


urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/plans')),
	url(r'^plans/', include('products.urls', namespace='home')),
    url(r'^professionals/', include('professionals.urls', namespace='professionals')),
    url(r'^accounts/$', RedirectView.as_view(url='/account')),
    url(r'^account/', include("accounts.urls", namespace='account')),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
    url(r'^search/', include("search.urls", namespace='search')),
    
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),


    url(r'^admin/', admin.site.urls),

    
#    url(r'^products/', include('products.urls', namespace='products')),
#    url(r'^professionals/', include('professionals.urls', namespace='professionals')),

]
