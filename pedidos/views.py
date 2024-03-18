from django.shortcuts import render
from .forms import FormularioCargaPedidos
from .models import CargarPedidos
import csv
from django.http import HttpResponse

def home(request):
    return render (request, 'home.html')

def soloform(request):
    return render (request, 'soloform.html')

def cargando_un_pedido(request):
    este_pedido = CargarPedidos()
    context = {'este_pedido': este_pedido}
    return render(request, 'pedido.html', context)

def exportar_a_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pedido.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'SKU',
        'Descripción',
        'Precio',
        'IVA',
    ])

    cargar_pedidos_data = CargarPedidos.objects.all()

    for pedido in cargar_pedidos_data:
        writer.writerow([
            pedido.subtotal,
            pedido.iva_10_5,
            pedido.iva_21,
            pedido.total,
        ])

    return response
