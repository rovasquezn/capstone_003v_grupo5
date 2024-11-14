# forms.py
from django import forms
from django.db import models
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
        fields = ['idReceta',
        # 'rutAtendedor',
        # 'rutTecnico',
        # 'rutAdministrador',
        'idOrdenTrabajo',
        'numeroOrdenTrabajo',
        'fechaEntregaOrdenTrabajo',
        'horaEntregaOrdenTrabajo',
        'laboratorioLejos',
        'gradoLejosOd',
        'gradoLejosOi',
        'prismaLejosOd',
        'prismaLejosOi',
        'adicionLejosOd',
        'adicionLejosOi',
        'tipoCristalLejos',
        'colorCristalLejos',
        'marcoLejos',
        'valorMarcoLejos',
        'valorCristalesLejos',
        'totalLejos',
        'altura',
        'laboratorioCerca',
        'gradoCercaOd',
        'gradoCercaOi',
        'prismaCercaOd',
        'prismaCercaOi',
        'adicionCercaOd',
        'adicionCercaOi',
        'tipoCristalCerca',
        'colorCristalCerca',
        'marcoCerca',
        'valorMarcoCerca',
        'valorCristalesCerca',
        'totalCerca',
        'totalOrdenTrabajo',
        'tipoPago',
        'numeroVoucherOrdenTrabajo',
        'observacionOrdenTrabajo']
             
             

    def __init__(self, *args, **kwargs):
        super(OrdenTrabajoForm, self).__init__(*args, **kwargs)
        # Si deseas agregar alguna clase de CSS específica, puedes hacerlo directamente en el ciclo.
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-sm'    
            field.widget.attrs.update({'class': 'form-control form-control-sm'})  # Clases para diseño 
            
            self.fields['idReceta'].widget = forms.TextInput()
            
            
            
            
            
        
        # # Configura el campo de fecha
        #     self.fields['fechaEntregaOrdenTrabajo'].widget = forms.DateInput(
        #         attrs={
        #             'class': 'form-control', 
        #             'type': 'date'
        #         }   
        #     )
       
       
        # Hacer los campos readonly 
        self.fields['numeroOrdenTrabajo'].widget.attrs['readonly'] = True 
        self.fields['totalLejos'].widget.attrs['readonly'] = True
        self.fields['totalCerca'].widget.attrs['readonly'] = True
        self.fields['totalOrdenTrabajo'].widget.attrs['readonly'] = True

        # 'rutAdministrador', 
        # 'rutTecnico', 
        # 'rutAtendedor', 
