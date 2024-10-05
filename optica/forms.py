# forms.py
from django import forms
from .models import Receta 

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta  # Asegúrate de vincular el formulario al modelo `Receta`
        fields = '__all__'  # O especifica los campos que quieras usar
        
    def __init__(self, *args, **kwargs):
        super(RecetaForm, self).__init__(*args, **kwargs)
        
        # Hacer los campos readonly
        self.fields['rutCliente'].widget = forms.TextInput()
        self.fields['rutCliente'].widget.attrs['readonly'] = True
        self.fields['rutCliente'].widget.attrs['readonly'] = True
        self.fields['dvRutCliente'].widget.attrs['readonly'] = True
        self.fields['nombreCliente'].widget.attrs['readonly'] = True
        self.fields['apPaternoCliente'].widget.attrs['readonly'] = True
        self.fields['apMaternoCliente'].widget.attrs['readonly'] = True
        self.fields['celularCliente'].widget.attrs['readonly'] = True
        self.fields['telefonoCliente'].widget.attrs['readonly'] = True