from django import forms
from django.contrib.auth.models import User
from datetime import date
from .models import Producto, CategoriaProducto, MovimientoInventario


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'stock': forms.NumberInput(attrs={'min': 0}),
            'stock_minimo': forms.NumberInput(attrs={'min': 0}),
            'categoria': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Seleccione una categoría"
        for name, field in self.fields.items():
            field.widget.attrs.setdefault('class', 'form-control')

    def clean_fecha_vencimiento(self):
        fecha = self.cleaned_data.get('fecha_vencimiento')
        if fecha and fecha < date.today():
            raise forms.ValidationError("La fecha de vencimiento no puede estar en el pasado.")
        return fecha

    def clean(self):
        cleaned_data = super().clean()
        stock = cleaned_data.get('stock')
        stock_minimo = cleaned_data.get('stock_minimo')

        if stock is not None and stock < 0:
            self.add_error('stock', "El stock no puede ser negativo.")
        if stock_minimo is not None and stock_minimo < 0:
            self.add_error('stock_minimo', "El stock mínimo no puede ser negativo.")
        return cleaned_data


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=False, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password or password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data


class MovimientoInventarioForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'tipo', 'cantidad', 'motivo']
        widgets = {
            'motivo': forms.TextInput(attrs={'placeholder': 'Motivo del movimiento'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
