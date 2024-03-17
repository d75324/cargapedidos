from django.db import models

class CargarPedidos(models.Model):
    
    sku_opciones = [
        ('CAB001', 'cab cero uno', 105.13, 21),
        ('CAB002', 'cab cero dos', 324,54, 21),
        ('CAB003', 'cab cero tres', 220,15, 10.5),
        ('CAB004', 'cab cero cuatro', 36,78, 10.5),
    ]

    sku = models.CharField(max_length=7, choices=sku_opciones)

    class Meta:
        app_label = 'Pedidos_1Hora'

    def __init__(self, sku, desc, price, iva):
        self.sku = sku
        self.desc = desc
        self.price = price
        self.iva = iva
    

