from django.shortcuts import render
from .models import Auto

# Create your views here.

def autos(request):
    autos = Auto.objects.all()
    context = {"autos" : autos}
    return render(request, "autos/autos.html", context)