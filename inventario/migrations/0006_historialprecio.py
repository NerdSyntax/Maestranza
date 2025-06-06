# Generated by Django 5.2.1 on 2025-05-26 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_producto_stock_producto_stock_minimo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialPrecio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historial_precios', to='inventario.producto')),
            ],
        ),
    ]
