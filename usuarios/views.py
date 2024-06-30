from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import usuario
from autos.models import Autos

# Create your views here.

def AgregarUsuario(request):

    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        contrasena = request.POST["contrasena"]
        nuevo_usuario = usuario.objects.create(username = username, email = email, contrasena = contrasena)
        nuevo_usuario.save()
        vehiculos = Autos.objects.all()
        context = {
        'vehiculos': vehiculos
        }
        return redirect('index')
    else:
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')

    context = {"form":form,}

    return render(request, "register/register.html", context)
