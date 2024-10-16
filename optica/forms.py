# forms.py
from django import forms
from .models import Receta 
from crispy_forms.helper import FormHelper

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta  # Asegúrate de vincular el formulario al modelo `Receta`
        fields = '__all__' 
        
    def __init__(self, *args, **kwargs):
        super(RecetaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-control-sm'
  
        # Hacer los campos readonly
        self.fields['rutCliente'].widget = forms.TextInput()
        self.fields['rutCliente'].widget.attrs['readonly'] = True
        self.fields['dvRutCliente'].widget.attrs['readonly'] = True
        self.fields['nombreCliente'].widget.attrs['readonly'] = True
        self.fields['apPaternoCliente'].widget.attrs['readonly'] = True
        self.fields['apMaternoCliente'].widget.attrs['readonly'] = True
        self.fields['celularCliente'].widget.attrs['readonly'] = True
        self.fields['telefonoCliente'].widget.attrs['readonly'] = True
        
  # Detectar si se trata de una edición o una creación
        # if self.instance and self.instance.pk:
            # Modo de edición - los campos del cliente son solo de lectura
        #     self.fields['rutCliente'].widget = forms.TextInput()
        #     self.fields['rutCliente'].widget.attrs['readonly'] = True
        #     self.fields['dvRutCliente'].widget.attrs['readonly'] = True
        #     self.fields['nombreCliente'].widget.attrs['readonly'] = True
        #     self.fields['apPaternoCliente'].widget.attrs['readonly'] = True
        #     self.fields['apMaternoCliente'].widget.attrs['readonly'] = True
        #     self.fields['celularCliente'].widget.attrs['readonly'] = True
        #     self.fields['telefonoCliente'].widget.attrs['readonly'] = True
        # else:
            # Modo de creación - el RUT se llenará con la búsqueda
            # self.fields['rutCliente'].widget = forms.TextInput()
            # self.fields['rutCliente'].widget.attrs['readonly'] = True