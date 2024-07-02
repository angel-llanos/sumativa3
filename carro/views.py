from django.shortcuts import render , redirect
from .carro import Carro
from autos.models import Autos
#create your views here

def agregar_autos(request, id_auto):

    carro = Carro(request)

    #Con esto obtenemos ya el producto que queremos 
    #agregar al carro
    autos=Autos.objects.get(id_auto=id_auto)

    #Ahora hay que agregar este producto al carro
    carro.agregar(autos=autos)

    return redirect("autos")

def eliminar_autos(request, id_auto):

    #Creamos el carro
    carro=Carro(request)

    autos=autos.objects.get(id_auto=id_auto)

    carro.eliminar(id_auto=id_auto)

    return redirect("autos")

def restar_autos(request, id_auto):

    carro=Carro(request)

    autos=Autos.objects.get(id_auto=id_auto)

    carro.restar_auto(autos=autos)

    return redirect("autos")

def limpiar_carro(request):

    carro=Carro(request)
    carro.limpiar_carro()

    return redirect("autos")

