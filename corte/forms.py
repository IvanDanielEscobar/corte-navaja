from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tu nombre'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tu telefono'})
        }