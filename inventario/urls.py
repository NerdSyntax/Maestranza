from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_inventario, name='registro'),
    path('registro-usuario/', views.registro_usuario, name='registro_usuario'),
    path('olvidar-contra/', views.olvidar_contra, name='olvidar_contra'),

    path('tienda/', views.tienda_view, name='tienda'),


    # CRUD de productos
    path('productos/registrar/', views.registro_producto, name='registro_producto'),
    path('productos/crud/', views.producto_crud, name='producto_crud'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    # CRUD de usuarios
    path('usuarios/', views.usuarios_crud, name='usuarios_crud'),
]
