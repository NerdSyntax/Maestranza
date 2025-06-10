from django.urls import path
from . import views
from .views import exportar_excel


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

    # Carrito
    path('carrito/', views.ver_carrito, name='ver_carrito'),

    # Historial precios
    path('productos/historial/<int:producto_id>/', views.historial_precios_producto, name='historial_precios'),

    # Movimientos de inventario
    path('movimientos/', views.listar_movimientos, name='listar_movimientos'),
    path('movimientos/registrar/', views.registrar_movimiento, name='registrar_movimiento'),
    path('productos/movimiento/<int:producto_id>/', views.registrar_movimiento_directo, name='registrar_movimiento_directo'),

    # Eliminación de historial y movimientos
    path('productos/eliminar-historial/<int:historial_id>/', views.eliminar_historial_precio, name='eliminar_historial_precio'),
    path('productos/eliminar-movimiento/<int:movimiento_id>/', views.eliminar_movimiento, name='eliminar_movimiento'),

    # Cambiar bodega
    path('producto/<int:producto_id>/cambiar_bodega/', views.cambiar_bodega, name='cambiar_bodega'),


    # Logout
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('exportar-excel/', exportar_excel, name='exportar_excel'),

    path('alerta-stock/', views.enviar_alerta_stock_bajo_view, name='enviar_alerta_stock_bajo'),
    path('', views.index, name='index'),

]
