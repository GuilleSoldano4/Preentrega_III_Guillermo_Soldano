from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def termotanques(request):
    productos = Producto.objects.filter(nombre__icontains='termotanque')
    return render(request, 'termotanques.html', {'productos': productos})

def luminarias(request):
    productos = Producto.objects.filter(nombre__icontains='luminaria')
    return render(request, 'luminarias.html', {'productos': productos})

def otros_productos(request):
    productos = Producto.objects.filter(nombre__icontains='cargador') | Producto.objects.filter(nombre__icontains='termo')
    return render(request, 'otros_productos.html', {'productos': productos})
