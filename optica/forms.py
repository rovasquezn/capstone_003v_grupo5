# forms.py
from django import forms
from .models import Receta, OrdenTrabajo 
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
            
            
class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo  # Asegúrate de vincular el formulario al modelo `Receta`
        fields = '__all__' 
        
    def __init__(self, *args, **kwargs):
        super(OrdenTrabajo, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-control-sm'
  
        # Hacer los campos readonly
        self.fields['idReceta'].widget = forms.TextInput()
        self.fields['rutCliente'].widget.attrs['readonly'] = True
        self.fields['dvRutCliente'].widget.attrs['readonly'] = True
        self.fields['nombreCliente'].widget.attrs['readonly'] = True
        self.fields['apPaternoCliente'].widget.attrs['readonly'] = True
        self.fields['apMaternoCliente'].widget.attrs['readonly'] = True
        self.fields['celularCliente'].widget.attrs['readonly'] = True
        self.fields['telefonoCliente'].widget.attrs['readonly'] = True       
        self.fields['numeroReceta'].widget.attrs['readonly'] = True
        self.fields['fechaReceta'].widget.attrs['readonly'] = True
        self.fields['lejosOdEsfera'].widget.attrs['readonly'] = True
        self.fields['lejosOdCilindro'].widget.attrs['readonly'] = True
        self.fields['lejosOdEje'].widget.attrs['readonly'] = True
        self.fields['lejosOiEsfera'].widget.attrs['readonly'] = True
        self.fields['lejosOiCilindro'].widget.attrs['readonly'] = True
        self.fields['lejosOiEje'].widget.attrs['readonly'] = True
        self.fields['dpLejos'].widget.attrs['readonly'] = True
        self.fields['cercaOdEsfera'].widget.attrs['readonly'] = True
        self.fields['cercaOdCilindro'].widget.attrs['readonly'] = True
        self.fields['cercaOdEje'].widget.attrs['readonly'] = True
        self.fields['cercaOiEsfera'].widget.attrs['readonly'] = True
        self.fields['cercaOiCilindro'].widget.attrs['readonly'] = True
        self.fields['cercaOiEje'].widget.attrs['readonly'] = True
        self.fields['dpCerca'].widget.attrs['readonly'] = True
        self.fields['tipoLente'].widget.attrs['readonly'] = True
        self.fields['institucion'].widget.attrs['readonly'] = True
        self.fields['doctorOftalmologo'].widget.attrs['readonly'] = True
        # self.fields['imagenReceta'].widget.attrs['readonly'] = True
        self.fields['observacionReceta'].widget.attrs['readonly'] = True
        self.fields['totalLejos'].widget.attrs['readonly'] = True
        self.fields['totalCerca'].widget.attrs['readonly'] = True
        self.fields['totalOrdenTrabajo'].widget.attrs['readonly'] = True

        # 'rutAdministrador', 
        # 'rutTecnico', 
        # 'rutAtendedor', 
