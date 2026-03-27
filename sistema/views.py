from django.shortcuts import render
from .models import Cliente, Producto, Venta

def inicio(request):
    return render(request, 'inicio.html')

def clientes(request):
    datos = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': datos})