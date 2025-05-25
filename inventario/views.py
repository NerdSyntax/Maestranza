from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login  # <-- ESTA LÍNEA ES CLAVE
from .models import Producto
from .forms import ProductoForm, UsuarioForm
from datetime import date, timedelta
def tienda_view(request):
    return render(request, 'inventario/tienda.html')
# Página de inicio
def index(request):
    return render(request, 'inventario/index.html')

# Formulario de login (sin lógica de autenticación todavía)
def login_view(request):
    return render(request, 'inventario/login.html')

# Página para registrar un ítem de inventario (puede ser temporal)
def registro_inventario(request):
    return render(request, 'inventario/registro_item.html')

# Registro individual de usuario (fuera del CRUD)
def registro_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            return render(request, 'inventario/registro_usuario.html', {
                'error': "Las contraseñas no coinciden."
            })

        if username and email and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=make_password(password)
                )
                return redirect('login')
            else:
                return render(request, 'inventario/registro_usuario.html', {
                    'error': "El nombre de usuario ya existe."
                })
    return render(request, 'inventario/registro_usuario.html')

# Vista visual para olvidar contraseña (puedes implementarla luego)
def olvidar_contra(request):
    return render(request, 'inventario/olvidar_contra.html')

# Vista para listar productos (opcional)
def lista_productos(request):
    productos = Producto.objects.all()
    today = date.today()
    today_plus_7 = today + timedelta(days=7)

    return render(request, 'inventario/lista_productos.html', {
        'productos': productos,
        'today': today,
        'today_plus_7': today_plus_7,
    })
# Formulario para registrar productos
def registro_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_crud')
    else:
        form = ProductoForm()
    return render(request, 'inventario/registro_producto.html', {'form': form})

# Vista para mostrar lista de productos y eliminar (CRUD parcial)
def producto_crud(request):
    productos = Producto.objects.all()

    if 'delete' in request.GET:
        producto = get_object_or_404(Producto, pk=request.GET['delete'])
        producto.delete()
        return redirect('producto_crud')

    return render(request, 'inventario/producto_crud.html', {'productos': productos})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto modificado exitosamente.")
            return redirect('producto_crud')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'inventario/registro_producto.html', {
        'form': form,
        'editar': True,
        'producto': producto
    })
# CRUD de usuarios (crear, editar, eliminar, listar)
def usuarios_crud(request):
    editar = False
    usuario = None

    if 'edit' in request.GET:
        editar = True
        usuario = get_object_or_404(User, pk=request.GET['edit'])
        form = UsuarioForm(request.POST or None, instance=usuario)
    elif 'delete' in request.GET:
        usuario = get_object_or_404(User, pk=request.GET['delete'])
        usuario.delete()
        messages.success(request, "Usuario eliminado exitosamente.")
        return redirect('usuarios_crud')
    else:
        form = UsuarioForm(request.POST or None)

    if request.method == 'POST':
        if editar:
            form = UsuarioForm(request.POST, instance=usuario)
        else:
            form = UsuarioForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Usuario guardado exitosamente.")
            return redirect('usuarios_crud')

    usuarios = User.objects.all()

    return render(request, 'inventario/usuarios_crud.html', {
        'form': form,
        'usuarios': usuarios,
        'editar': editar,
        'usuario': usuario
    })
@login_required
def tienda_view(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/tienda.html', {'productos': productos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tienda')  # Redirige directamente a la tienda
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'inventario/login.html')

# --
def ver_carrito(request):
    return render(request, 'inventario/carrito.html')

