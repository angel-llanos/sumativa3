from django.shortcuts import render , redirect
from .carro import Carro
from autos.models import Autos
#create your views here

def agregar_autos(request, id_autos):

    carro = Carro(request)

    #Con esto obtenemos ya el producto que queremos 
    #agregar al carro
    Autos=Autos.objects.get(id=id_autos)
    imagen_url = Autos.imagen.url

    print(carro)

    #Ahora hay que agregar este producto al carro
    carro.agregar(autos=Autos)

    return redirect("autos")

def eliminar_autos(request, id_autos):

    #Creamos el carro
    carro=Carro(request)

    autos=autos.objects.get(id=id_autos)

    carro.eliminar(id=id_autos)

    return redirect("autos")

def restar_autos(request, id_autos):

    carro=Carro(request)

    autos=autos.objects.get(id=id_autos)

    carro.restar_autos(id=id_autos)

    return redirect("autos")

def limpiar_carro(request):

    carro=Carro(request)
    carro.limpiar_carro()

    return redirect("autos")

