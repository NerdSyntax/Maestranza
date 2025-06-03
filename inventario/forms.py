from django import forms
from django.contrib.auth.models import User
from datetime import date
from .models import Producto, CategoriaProducto, MovimientoInventario, Bodega


from django import forms
from datetime import date
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'stock': forms.NumberInput(attrs={'min': 0}),
            'stock_minimo': forms.NumberInput(attrs={
                'min': 0,
                'readonly': 'readonly',
                'placeholder': '5'
            }),
            'categoria': forms.Select(),
            'bodega': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🔒 Valor fijo de stock mínimo
        self.fields['stock_minimo'].initial = 5
        self.fields['stock_minimo'].disabled = True

        # Etiquetas vacías
        self.fields['categoria'].empty_label = "Seleccione una categoría"
        self.fields['bodega'].empty_label = "Seleccione una bodega"

        # Bootstrap classes
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
        stock_minimo = 5  # Valor fijo esperado

        if stock is not None and stock < stock_minimo:
            self.add_error('stock', f"El stock no puede ser menor al stock mínimo ({stock_minimo}).")

        # 🔐 Reforzar que el stock mínimo no pueda ser sobreescrito
        cleaned_data['stock_minimo'] = stock_minimo

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
