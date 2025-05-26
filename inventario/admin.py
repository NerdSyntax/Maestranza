from django.contrib import admin
from .models import Proveedor, CategoriaProducto, Producto, MovimientoInventario


# Register your models here.

admin.site.register(Proveedor)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(MovimientoInventario)

