from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Cliente

def inicio(request):
    
    clientes = Cliente.objects.all()
    return render(request, 'inicio.html', {'clientes':clientes})

def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        documento = request.POST.get('documento')
        localidad = request.POST.get('localidad')
        cliente = Cliente(nombre=nombre, apellido=apellido, documento=documento, localidad=localidad)
        cliente.save()
    return render(request, 'crear_cliente.html',{})

def lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista.html', {'clientes':clientes})
