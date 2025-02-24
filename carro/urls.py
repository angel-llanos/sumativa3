from django.urls import path

from . import views

app_name = "carro" #esto es un namespace

urlpatterns = [
    path("agregar/<int:id_auto>/", views.agregar_autos, name="agregar"),
    path("eliminar/<int:id_auto>/", views.eliminar_autos, name="eliminar"),
    path("restar/<int:id_auto>/", views.restar_autos, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]
