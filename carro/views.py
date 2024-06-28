from django.shortcuts import render
from .models import carro

# Create your views here.

def carro(request):
    carro = carro.objects.all()
    context = {"carro" : carro}
    return render(request, "carro/carrito.html", context)