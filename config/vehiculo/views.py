from django.shortcuts import render, redirect
from .forms import VehiculoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Vehiculo

# Create your views here.

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculo.html', {'vehiculos': vehiculos})


@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    if request.method =='POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form':form})
    
