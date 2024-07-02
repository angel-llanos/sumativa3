from django.urls import path
from . import views

urlpatterns = [
    path('autos', views.autos , name="autos"),
    path('register/', views.register , name="register"),
    path('exit', views.exit , name="exit"),
    path('descripcion/<int:id_auto>', views.descripcion, name="descripcion")
]
