from django.shortcuts import render
from .models import Autos

# Create your views here.

def autos(request):
    autos = Autos.objects.all()
    return render(request, "autos/autos.html", {

        "autos":autos

    })