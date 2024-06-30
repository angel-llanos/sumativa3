from django.shortcuts import render
from autos.models import Autos
# Create your views here.

def index(request):
    vehiculos = Autos.objects.all()
    context = {
        'vehiculos': vehiculos
    }
    return render(request, "menu/index.html", context)