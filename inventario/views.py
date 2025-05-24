from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def index(request):
    return render(request, 'inventario/index.html')

def login_view(request):
    return render(request, 'inventario/login.html')

def registro_inventario(request):
    return render(request, 'inventario/registro_item.html')

def registro_usuario(request):
    return render(request, 'inventario/registro_usuario.html')

def olvidar_contra(request):
    return render(request, 'inventario/olvidar_contra.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/producto_form.html', {'form': form})
