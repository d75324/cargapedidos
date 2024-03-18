from django.db import models

class CargarPedidos(models.Model):
    
    sku_opciones = [
        ('CAB001', 'cab cero uno', 105.13, 21),
        ('CAB002', 'cab cero dos', 324,54, 21),
        ('CAB003', 'cab cero tres', 220,15, 10.5),
        ('CAB004', 'cab cero cuatro', 36,78, 10.5),
    ]

    sku = models.CharField(max_length=7, choices=sku_opciones)
    desc = models.CharField(max_length=100)
    qty = models.IntegerField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        app_label = 'Pedidos_1Hora'
    
    # va a retornar la suma de los precios (price x qty) sin IVA
    def subtotal():
        pass

    # va a retornar el iva encapsulado: el total para 10,5% y el total para 21%
    def iva105y21():
        pass
    
    # va a retornar la suma de subtotal, iva de 10,5 e iva de 21%
    def total():
        pass