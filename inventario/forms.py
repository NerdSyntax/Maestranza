from django import forms
from django.contrib.auth.models import User
from .models import Producto
from datetime import date
from .models import MovimientoInventario
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'stock': forms.NumberInput(attrs={'min': 0}),
            'stock_minimo': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_fecha_vencimiento(self):
        fecha = self.cleaned_data.get('fecha_vencimiento')
        if fecha and fecha < date.today():
            raise forms.ValidationError("La fecha de vencimiento no puede estar en el pasado.")
        return fecha

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

    def clean_stock_minimo(self):
        minimo = self.cleaned_data.get('stock_minimo')
        if minimo is not None and minimo < 0:
            raise forms.ValidationError("El stock mínimo no puede ser negativo.")
        return minimo


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
        super(MovimientoInventarioForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'