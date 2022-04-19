from django.urls import path
from .views import *
from django.views.generic import RedirectView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('index', Index.as_view(), name='Index'),
    path('registro', Registro.as_view(), name='Registro'),
    path('', RedirectView.as_view(url=''))
]
