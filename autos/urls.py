from django.urls import path
from . import views

urlpatterns = [
    path('autos', views.autos , name="autos"),
]
