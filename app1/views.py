from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from app1.models import *
from app1.forms import *
# Create your views here.

def crearveterinario(request):
    if request.method == 'POST':
        form = FormularioVeterinario(request.POST)
        if form.is_valid():
            
            nombre = form.cleaned_data['nombre_vet']
            apellido = form.cleaned_data['apellido_vet']
            telefono = form.cleaned_data['telefono_vet']
            legajo = form.cleaned_data['legajo']
            veterinario = Veterinario(nombre_vet=nombre, apellido_vet=apellido, telefono_vet=telefono, legajo=legajo)
            veterinario.save()  # Guardar en la base de datos
            return render(request, 'index.html')
    else:
        form = FormularioVeterinario()
        return render(request, 'crearveterinario.html', {'form': form})

def crearcliente(request):
    if request.method == 'POST':
        form = FormularioCliente(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre_cli']
            apellido = form.cleaned_data['apellido_cli']
            telefono = form.cleaned_data['telefono_cli']
            mail = form.cleaned_data['mail']
            cliente = Cliente(nombre_cli=nombre, apellido_cli=apellido, telefono_cli=telefono, mail=mail)
            cliente=form.save()
            return redirect('index.html')
    else:
        form = FormularioCliente()
        return render(request, 'crearcliente.html', {'form': form})

def crearmascota(request):
    form = FormularioMascota()
    if form.is_valid():
        nombre = form.cleaned_data['nombre_mas']
        raza = form.cleaned_data['raza']
        edad = form.cleaned_data['edad']
        dueño = form.cleaned_data['dueño']
        mascota = Animal(nombre_mas=nombre, raza=raza, edad=edad, dueño=dueño)
        mascota=form.save()
        return redirect('index.html')
    else:
        form = FormularioMascota()
        return render(request, 'crearmascota.html', {'form': form})

def buscarmascota(request):
    mascota = []
    form = MascotaSearchForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            mascota = Animal.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscarmascota.html', {'form': form, 'mascota': mascota})


def index(request):
    return render(request, 'index.html')
