from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_inventario, name='registro'),
    path('registro-usuario/', views.registro_usuario, name='registro_usuario'),
    path('olvidar-contra/', views.olvidar_contra, name='olvidar_contra'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
]
