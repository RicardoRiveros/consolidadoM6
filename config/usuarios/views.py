from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .forms import RegistroUsuarioForm
from django.contrib.auth.models import Permission
from vehiculo.models import Vehiculo
from django.contrib.contenttypes.models import ContentType


# Create your views here.
def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data= request.POST )
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Se ha iniciado sesión con éxito')
            return redirect('index')
    
    else:
        form =  AuthenticationForm()

    return render(request,'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada con éxito')
    return redirect('usuarios:login')



@login_required
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()  # Guardar el usuario

            # Asignar permiso y crear contexto
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permiso = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
            usuario.user_permissions.add(permiso)

            context = {'form': form, 'user': usuario}  # Añadir 'user' al contexto
            return render(request, 'usuarios/registro.html', context)
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})
            