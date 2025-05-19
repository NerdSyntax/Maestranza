from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'inventario/index.html')

def login_view(request):
    return render(request, 'inventario/login.html')

def registro_inventario(request):
    return render(request, 'inventario/registro.html')
