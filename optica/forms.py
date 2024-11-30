# forms.py
from django import forms
from django.db import models
from .models import Receta, OrdenTrabajo, CustomUser
from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser, Cliente, Administrador, Atendedor, Tecnico, Receta, OrdenTrabajo
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    ap_paterno = forms.CharField(label='Apellido Paterno', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    ap_materno = forms.CharField(label='Apellido Materno', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    rut = forms.CharField(label='RUN', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'pattern': '\d{7,8}', 'title': 'El RUT debe tener entre 7 y 8 dígitos.', 'maxlength': '8'}), initial='')
    dv = forms.CharField(label='DV', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'pattern': '[0-9Kk]', 'maxlength': '1', 'title': 'El DV debe ser un número o la letra K.'}), initial='')
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}))
    celular = forms.CharField(label='Celular', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'pattern': '\d{9}', 'maxlength': '9', 'title': 'El celular debe tener 9 dígitos.'}), initial='')
    user_type = forms.ChoiceField(label='Tipo de Usuario', choices=[('', '---'), (1, 'Administrador'), (2, 'Atendedor'), (3, 'Técnico')], widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required', 'minlength': '8', 'title': 'La contraseña debe tener al menos 8 caracteres.'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required', 'minlength': '8', 'title': 'Las contraseñas deben coincidir.'}))
    is_active = forms.ChoiceField(
        label='Estado',
        choices=[(True, 'Activo'), (False, 'Inactivo')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'ap_paterno', 'ap_materno', 'rut', 'dv', 'email', 'celular', 'user_type', 'username', 'password1', 'password2', 'is_active']

    def clean(self):
        cleaned_data = super().clean()
        rut = cleaned_data.get("rut")
        dv = cleaned_data.get("dv")
        email = cleaned_data.get("email")
        username = cleaned_data.get("username")
        

        # Validar RUT y DV juntos
        if CustomUser.objects.filter(rut=rut, dv=dv).exists():
            self.add_error('rut', "Ya existe Usuario con este RUN y DV.")
            

        # # Validar Email
        # if CustomUser.objects.filter(email=email).exists():
        #     raise forms.ValidationError("El correo electrónico ya existe en el sistema.")

        return cleaned_data

    def clean_username(self):
        first_name = self.cleaned_data.get('first_name', '').lower()
        ap_paterno = self.cleaned_data.get('ap_paterno', '').lower()
        username = f"{first_name[0]}.{ap_paterno}"
        return username

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    ap_paterno = forms.CharField(label='Apellido Paterno', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    ap_materno = forms.CharField(label='Apellido Materno', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}))
    rut = forms.CharField(label='RUT', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'pattern': '\d{7,8}', 'title': 'El RUT debe tener entre 7 y 8 dígitos.'}))
    dv = forms.CharField(label='DV', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'pattern': '[0-9Kk]', 'maxlength': '1', 'title': 'El DV debe ser un número o la letra K.'}))
    celular = forms.CharField(label='Celular', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'pattern': '\d{9}', 'maxlength': '9', 'title': 'El celular debe tener 9 dígitos.'}))
    user_type = forms.ChoiceField(label='Tipo de Usuario', choices=[(1, 'Administrador'), (2, 'Atendedor'), (3, 'Técnico')], widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))
    is_active = forms.ChoiceField(
        label='Estado',
        choices=[(True, 'Activo'), (False, 'Inactivo')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'ap_paterno', 'ap_materno', 'email', 'rut', 'dv', 'celular', 'user_type', 'is_active', 'username']
          

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

# Mi Perfil
class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'ap_paterno', 'ap_materno', 'rut', 'dv', 'email', 'celular', 'username', 'user_type')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ap_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'ap_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'dv': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Nombre',
            'ap_paterno': 'Apellido Paterno',
            'ap_materno': 'Apellido Materno',
            'rut': 'RUT',
            'dv': 'DV',
            'email': 'Correo Electrónico',
            'celular': 'Celular',
            'username': 'Nombre de Usuario',
            'user_type': 'Tipo de Usuario',
        }

    class Meta:
        model = CustomUser
        fields = ['username']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

class AtendedorForm(forms.ModelForm):
    class Meta:
        model = Atendedor
        fields = '__all__'

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = '__all__'

class AdministradorChangeForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ('rutAdministrador', 'dvRutAdministrador', 'nombreAdministrador', 'apPaternoAdministrador', 'apMaternoAdministrador', 'celularAdministrador', 'emailAdministrador')

class AtendedorChangeForm(forms.ModelForm):
    class Meta:
        model = Atendedor
        fields = ['rutAtendedor', 'dvRutAtendedor']
        widgets = {
            'rutAtendedor': forms.TextInput(attrs={'class': 'form-control'}),
            'dvRutAtendedor': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TecnicoChangeForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ('rutTecnico', 'dvRutTecnico', 'nombreTecnico', 'apPaternoTecnico', 'apMaternoTecnico', 'celularTecnico', 'emailTecnico')
        widgets = {
            'rutTecnico': forms.TextInput(attrs={'readonly': 'readonly'}),
            'dvRutTecnico': forms.TextInput(attrs={'readonly': 'readonly'}),
        }



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
        # if self.instance && self.instance.pk:
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


class AdministradorCreationForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ('rutAdministrador', 'dvRutAdministrador', 'nombreAdministrador', 'apPaternoAdministrador', 'apMaternoAdministrador', 'celularAdministrador', 'emailAdministrador')

class AtendedorCreationForm(forms.ModelForm):
    class Meta:
        model = Atendedor
        fields = ('rutAtendedor', 'dvRutAtendedor', 'nombreAtendedor', 'apPaternoAtendedor', 'apMaternoAtendedor', 'celularAtendedor', 'emailAtendedor')

class TecnicoCreationForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ('rutTecnico', 'dvRutTecnico', 'nombreTecnico', 'apPaternoTecnico', 'apMaternoTecnico', 'celularTecnico', 'emailTecnico')
