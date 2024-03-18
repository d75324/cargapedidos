from django import forms
from .models import CargarPedidos

class FormularioCargaPedidos(forms.ModelForm):
    class Meta:
        model = CargarPedidos
        fields = [
            "sku",
            "desc",
            "price",
            "iva",
        ]