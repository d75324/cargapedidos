from django.shortcuts import render
from .forms import FormularioCargaPedidos
from .models import CargarPedidos

def home(request):
    return render (request, 'home.html')

def soloform(request):
    return render (request, 'soloform.html')

def cargando_un_pedido(request):
    este_pedido = CargarPedidos()
    context = {'este_pedido': este_pedido}
    return render(request, 'pedido.html', context)
