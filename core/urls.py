from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('index', Index.as_view(), name='Index'),
    path('registro', Registro.as_view(), name='Registro'),
]
