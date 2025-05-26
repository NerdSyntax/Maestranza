from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='productos'
    )
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=1)

    serial_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        blank=True,
        help_text="Número de serie generado automáticamente"
    )

    def save(self, *args, **kwargs):
        if not self.serial_number:
            self.serial_number = self.generar_serial_unico()
        super().save(*args, **kwargs)

    def generar_serial_unico(self):
        year = now().year
        prefix = f"INV-{year}-"
        last_product = Producto.objects.filter(serial_number__startswith=prefix).order_by('id').last()
        if last_product:
            last_number = int(last_product.serial_number.split("-")[-1])
        else:
            last_number = 0
        new_serial = f"{prefix}{last_number + 1:05d}"
        while Producto.objects.filter(serial_number=new_serial).exists():
            last_number += 1
            new_serial = f"{prefix}{last_number + 1:05d}"
        return new_serial

    def __str__(self):
        return f"{self.nombre} [{self.serial_number}]"


class HistorialPrecio(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='historial_precios'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Usuario que modificó el precio"
    )
    rol = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Rol del usuario que hizo el cambio"
    )

    def __str__(self):
        return f"{self.producto.nombre} - ${self.precio} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"


class MovimientoInventario(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=255, blank=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Usuario que registró el movimiento"
    )
    rol = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Rol del usuario que hizo el movimiento"
    )

    def __str__(self):
        return f"{self.tipo.title()} - {self.producto.nombre} - {self.cantidad}"
