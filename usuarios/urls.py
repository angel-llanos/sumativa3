from django.urls import path
from . import views

urlpatterns = [
    path('register', views.AgregarUsuario , name="register"),
]
