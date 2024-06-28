from django.urls import path
from . import views

urlpatterns = [
    path('carro', views.carro , name="carro"),
]
