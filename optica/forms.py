# forms.py
from django import forms
from .models import Receta 

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta  # Asegúrate de vincular el formulario al modelo `Receta`
        fields = '__all__'  # O especifica los campos que quieras usar