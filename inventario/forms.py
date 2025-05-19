from django import forms
from .models import Producto, CategoriaProducto, Proveedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'numero_serie', 'categoria', 'ubicacion', 'cantidad_en_stock', 'proveedor', 'lote', 'fecha_vencimiento', 'precio_compra']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }
