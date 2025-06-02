# inventario/utils.py

from django.core.mail import send_mail
from django.conf import settings
from .models import Producto
from django.db.models import F

def enviar_alerta_stock_bajo():
    productos_bajos = Producto.objects.filter(stock__lte=F('stock_minimo'))

    if not productos_bajos.exists():
        return

    mensaje = "⚠️ Alerta de productos con stock bajo:\n\n"
    for p in productos_bajos:
        mensaje += f"• {p.nombre} — Stock actual: {p.stock} (mínimo requerido: {p.stock_minimo})\n"

    send_mail(
        subject="📦 Alerta de Stock Bajo - Maestranza",
        message=mensaje,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[
            "jose.oporto.va@gmail.com",
            "oscarvizcaya9@gmail.com"
        ],
        fail_silently=False
    )
