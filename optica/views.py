from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.db.models import Q, Max, QuerySet
from typing import Any
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import (
    AdministradorChangeForm, AdministradorCreationForm, AtendedorChangeForm, AtendedorCreationForm, CustomUserCreationForm, CustomUserChangeForm, 
    CustomPasswordChangeForm, RecetaForm, OrdenTrabajoForm, TecnicoChangeForm, TecnicoCreationForm, UserProfileForm
)
from .models import Cliente, Receta, OrdenTrabajo, Administrador, Atendedor, Tecnico, CustomUser
from datetime import datetime
from optica import models
from django.http import JsonResponse
from .signals import send_password_reset_success_email, send_user_creation_email


User = get_user_model()


# Funciones auxiliares
def get_profile_and_form(user):
    """Devuelve el perfil asociado al usuario y el formulario correspondiente."""
    if user.user_type == 1:
        return getattr(user, 'administrador', None), AdministradorChangeForm
    elif user.user_type == 2:
        return getattr(user, 'atendedor', None), AtendedorChangeForm
    elif user.user_type == 3:
        return getattr(user, 'tecnico', None), TecnicoChangeForm
    return None, None

@login_required
def index(request):
    user = request.user
    last_name_parts = user.last_name.split()
    apellido_paterno = last_name_parts[0] if last_name_parts else ''
    nombre_completo = f"{user.first_name} {apellido_paterno}"  # Solo el apellido paterno
    context = {
        'nombre_completo': nombre_completo,
    }
    return render(request, 'optica/index.html', context)

@login_required
def mi_perfil(request):
    user = request.user
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña ha sido cambiada con éxito.')
            return redirect('mi_perfil')
        else:
            messages.error(request, 'Por favor, corrige los errores a continuación.')
    else:
        password_form = PasswordChangeForm(user=request.user)
    
    context = {
        'first_name': user.first_name,
        'ap_paterno': user.ap_paterno,
        'ap_materno': user.ap_materno,
        'rut': f"{user.rut}-{user.dv}",
        'email': user.email,
        'celular': user.celular,
        'username': user.username,
        'user_type': user.get_user_type_display(),
        'password_form': password_form,
    }
    return render(request, 'optica/mi_perfil.html', context)

class CustomLoginView(LoginView):
    template_name = 'optica/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Redirige a la página de inicio si el usuario ya está autenticado
        return super().dispatch(request, *args, **kwargs)

#Restablecer contraseña
class CustomPasswordResetView(PasswordResetView):
    template_name = 'optica/password_reset.html'
    email_template_name = 'optica/password_reset_email.html'
    subject_template_name = 'optica/password_reset_subject.txt'  # Añadir esta línea
    html_email_template_name = 'optica/password_reset_email.html'  # Añadir esta línea
    success_url = reverse_lazy('password_reset_done')

#Envio de mail confirmando restablecimiento de contraseña
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('password_reset_complete')

    def form_valid(self, form):
        user = form.save()
        send_password_reset_success_email(user)
        return super().form_valid(form)

# Clientes
class ListarClienteView(LoginRequiredMixin, generic.ListView):
    model = Cliente
    paginate_by = 8
    ordering = ['-creacionCliente']  # Ordena por el campo 'creacionCliente' en orden descendente
    #Agregados por Derek para limitar vistas por tipo de suario
    #template_name = 'optica/cliente_list.html'
    #context_object_name = 'clientes'
    # def get_queryset(self) -> QuerySet[Any]:
    #     q = self.request.GET.get('q')

    #     if q:
    #         return Cliente.objects.filter(
    #             Q(nombreCliente__icontains=q) | Q(apPaternoCliente__icontains=q)| Q(rutCliente__icontains=q))
        
    #     return super().get_queryset()
    
    
    
    def get_queryset(self):
        q = self.request.GET.get('q')

        queryset = super().get_queryset()

        if q:
            queryset = queryset.filter(
                Q(nombreCliente__icontains=q) |
                Q(apPaternoCliente__icontains=q) |
                Q(rutCliente__icontains=q)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')  # Mantener el valor de la búsqueda en el contexto
        return context
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type in [1, 2, 3]  # Administrador, Atendedor y Técnico

class CrearClienteView(SuccessMessageMixin, generic.CreateView):
    model = Cliente
    fields = ('rutCliente', 
    'dvRutCliente', 
    'nombreCliente',
    'apPaternoCliente',
    'apMaternoCliente', 
    'celularCliente',
    'telefonoCliente', 
    'emailCliente',
    'direccionCliente',)
    success_url = reverse_lazy('cliente_list')
    success_message = "El cliente se ha creado exitosamente."
    


class EditarClienteView(SuccessMessageMixin, generic.UpdateView):
    model = Cliente
    fields = ('nombreCliente',
    'apPaternoCliente',
    'apMaternoCliente', 
    'celularCliente',
    'telefonoCliente', 
    'emailCliente',
    'direccionCliente',)
    success_url = reverse_lazy('cliente_list')
    success_message = "El cliente se ha editado exitosamente."

class EliminarClienteView(SuccessMessageMixin, generic.DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')
    success_message = "El cliente se ha eliminado exitosamente."

# Recetas
class ListarRecetaView(generic.ListView):
    model = Receta
    paginate_by = 8
    ordering = ['-creacionReceta']
    
    
    def get_queryset(self) -> QuerySet[Any]: 
        q = self.request.GET.get('q')
        if q:
            return Receta.objects.filter(
                Q(rutCliente__nombreCliente__icontains=q) | 
                Q(rutCliente__apPaternoCliente__icontains=q) | 
                Q(rutCliente__rutCliente__icontains=q)
            )
        return super().get_queryset()

class CrearRecetaView(SuccessMessageMixin, generic.CreateView):
    model = Receta
    fields = ('idReceta',
    'rutCliente',
    'dvRutCliente',
    'nombreCliente',
    'apPaternoCliente',
    'apMaternoCliente',
    'celularCliente',
    'telefonoCliente',
    # 'rutAdministrador', 
    'rutTecnico', 
    'rutAtendedor', 
    'numeroReceta', 
    'fechaReceta', 
    'lejosOdEsfera', 
    'lejosOdCilindro', 
    'lejosOdEje', 
    'lejosOiEsfera', 
    'lejosOiCilindro',
    'lejosOiEje', 
    'dpLejos', 
    'cercaOdEsfera', 
    'cercaOdCilindro', 
    'cercaOdEje', 
    'cercaOiEsfera', 
    'cercaOiCilindro', 
    'cercaOiEje',
    'dpCerca', 
    'tipoLente',
    'institucion',
    'doctorOftalmologo',
    'imagenReceta',
    'observacionReceta',)
    
    
    widgets = {
            'imagenReceta': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    success_url = reverse_lazy('receta_list')
    success_message = "La receta se ha creado exitosamente."


    template_name = 'optica/receta_form.html'  # Cambia esto al nombre de tu template
    
    def get(self, request):
        cliente = None
        rut_cliente = request.GET.get('rut_cliente')
        
        # Buscar cliente por RUT
        if rut_cliente:
            try:
                cliente = Cliente.objects.get(rutCliente=rut_cliente)
                messages.success(request, "Cliente encontrado")
            except Cliente.DoesNotExist:
                cliente = None
                messages.error(request, "Cliente no encontrado")
        
        # Cargar formulario de receta con datos del Cliente, si existe cliente, se pueden prellenar campos
        form = RecetaForm(initial={
            'rutCliente': cliente.rutCliente if cliente else '',
            'dvRutCliente': cliente.dvRutCliente if cliente else '', 
            'nombreCliente': cliente.nombreCliente if cliente else '',
            'apPaternoCliente': cliente.apPaternoCliente if cliente else '',
            'apMaternoCliente': cliente.apMaternoCliente if cliente else '',
            'celularCliente': cliente.celularCliente if cliente else '',
            'telefonoCliente': cliente.telefonoCliente if cliente else '',
        })
    
        return render(request, self.template_name, {'form': form, 'cliente': cliente})


    def post(self, request):
        form = RecetaForm(request.POST, request.FILES)
        
        if form.is_valid():
            receta = form.save()  # Guardar la receta
            messages.success(request, self.success_message)  # Añadir el mensaje de éxito
            return redirect(self.success_url)  # Redirige a la lista de recetas
        
        return render(request, self.template_name, {'form': form})
    

class EditarRecetaView(SuccessMessageMixin, generic.UpdateView):
    model = Receta
    fields = ('numeroReceta', 
    'fechaReceta', 
    'lejosOdEsfera', 
    'lejosOdCilindro', 
    'lejosOdEje', 
    'lejosOiEsfera', 
    'lejosOiCilindro',
    'lejosOiEje', 
    'dpLejos', 
    'cercaOdEsfera', 
    'cercaOdCilindro', 
    'cercaOdEje', 
    'cercaOiEsfera', 
    'cercaOiCilindro', 
    'cercaOiEje',
    'dpCerca', 
    'tipoLente',
    'institucion',
    'doctorOftalmologo',
    'imagenReceta',
    'observacionReceta'
    )
    success_url = reverse_lazy('receta_list')
    success_message = "La receta se ha editado exitosamente."


class EliminarRecetaView(SuccessMessageMixin, generic.DeleteView):
    model = Receta
    success_url = reverse_lazy('receta_list')
    success_message = "La receta se ha eliminado exitosamente."

# Órdenes de Trabajo
class ListarOrdenTrabajoView(generic.ListView):
    model = OrdenTrabajo
    paginate_by = 8
    ordering = ['-fechaOrdenTrabajo']
    
    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')
        if q:
            return OrdenTrabajo.objects.filter(
                Q(idReceta__rutCliente__nombreCliente__icontains=q) | 
                Q(idReceta__rutCliente__apPaternoCliente__icontains=q) | 
                Q(idReceta__rutCliente__rutCliente__icontains=q)
            )
        return super().get_queryset()
 
    
    # def get_queryset(self) -> QuerySet[Any]: 
    #     q = self.request.GET.get('q')
    #     if q:
    #         return OrdenTrabajo.objects.filter(
    #             Q(idReceta__rutCliente__cliente__nombreCliente__icontains=q) | 
    #             Q(idReceta__rutCliente__cliente__apPaternoCliente__icontains=q) | 
    #             Q(idReceta__rutCliente__rutCliente__icontains=q)
    #         )
    #     return super().get_queryset()

class CrearOrdenTrabajoView(SuccessMessageMixin, generic.CreateView):
    model = OrdenTrabajo
    fields = (
    'idReceta',
    # 'rutAdministrador', 
    'rutTecnico', 
    'rutAtendedor', 
    'idOrdenTrabajo',
    'numeroOrdenTrabajo',
    # 'fechaOrdenTrabajo'
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
    'observacionOrdenTrabajo'
    )
    
    success_url = reverse_lazy('ordenTrabajo_list')
    success_message = "La Orden de Trabajo se ha creado exitosamente."
    template_name = 'optica/ordenTrabajo_form.html'  # Cambia esto al nombre de tu template
    

    def generar_numero_orden(self):
        # Lógica para calcular el siguiente número de orden
        ultimo_valor = OrdenTrabajo.objects.aggregate(max_val=Max('numeroOrdenTrabajo'))['max_val']
        return (ultimo_valor + 1) if ultimo_valor and ultimo_valor >= 6000 else 6000

    def get(self, request):
        receta = None
        id_receta = request.GET.get('id_receta')

        if id_receta:
            try:
                receta = Receta.objects.get(idReceta=id_receta)
                messages.success(request, "Receta encontrada") 
            except Receta.DoesNotExist:
                messages.error(request, "Receta no encontrada")

        numero_orden = self.generar_numero_orden()



        # # Inicializa el formulario con el número de orden y la receta si está presente
        # form = OrdenTrabajoForm(initial={
        #     'numeroOrdenTrabajo': numero_orden,
        #     'idReceta': receta.idReceta if receta else None
        # })

        # return render(request, self.template_name, {
        #     'form': form,
        #     'receta': receta
        # })
    
    
    
    
        form = OrdenTrabajoForm(initial={  
            'numeroOrdenTrabajo': numero_orden,
            'idReceta': receta.idReceta if receta else '',
                                   
            'rutCliente': receta.rutCliente if receta else '',
            'dvRutCliente': receta.dvRutCliente if receta else '',
            'nombreCliente': receta.nombreCliente if receta else '',
            'apPaternoCliente': receta.apPaternoCliente if receta else '',
            'apMaternoCliente': receta.apMaternoCliente if receta else '',
            'celularCliente': receta.celularCliente if receta else '',
            'telefonoCliente': receta.telefonoCliente if receta else '',
            # # 'rutAdministrador', 
            # # 'rutTecnico', 
            # # 'rutAtendedor', 
            'numeroReceta': receta.numeroReceta if receta else '', 
            'fechaReceta': receta.fechaReceta if receta else '', 
            'lejosOdEsfera': receta.lejosOdEsfera if receta else '', 
            'lejosOdCilindro': receta.lejosOdCilindro if receta else '', 
            'lejosOdEje': receta.lejosOdEje if receta else '', 
            'lejosOiEsfera': receta.lejosOiEsfera if receta else '', 
            'lejosOiCilindro': receta.lejosOiCilindro if receta else '',
            'lejosOiEje': receta.lejosOiEje if receta else '', 
            'dpLejos': receta.dpLejos if receta else '', 
            'cercaOdEsfera': receta.cercaOdEsfera if receta else '', 
            'cercaOdCilindro': receta.cercaOdCilindro if receta else '', 
            'cercaOdEje': receta.cercaOdEje if receta else '', 
            'cercaOiEsfera': receta.cercaOiEsfera if receta else '', 
            'cercaOiCilindro': receta.cercaOiCilindro if receta else '', 
            'cercaOiEje': receta.cercaOiEje if receta else '',
            'dpCerca': receta.dpCerca if receta else '', 
            'tipoLente': receta.tipoLente if receta else '',
            'institucion': receta.institucion if receta else '',
            'doctorOftalmologo': receta.doctorOftalmologo if receta else '',
            'observacionReceta': receta.observacionReceta if receta else '',           
            })
    
        return render(request, self.template_name, {'form': form, 'receta': receta})
    
    

    def post(self, request):
        form = OrdenTrabajoForm(request.POST)
        receta = None 
        id_receta = request.GET.get('id_receta')  # Captura el `id_receta` del parámetro de consulta

        if id_receta:
            try:
                # Obtén la receta con el `id_receta` proporcionado
                receta = Receta.objects.get(idReceta=id_receta)
                
                if form.is_valid():
                    orden_trabajo = form.save(commit=False)
                    orden_trabajo.idReceta = receta  # Asigna la receta a la orden de trabajo
                    orden_trabajo.save()  # Guarda la orden de trabajo
                    
                    messages.success(request, "Orden de Trabajo creada con éxito.")
                    return redirect(self.success_url)  # Redirige tras guardar
                    
            except Receta.DoesNotExist:
                messages.error(request, "Receta no encontrada.")
        else:
            messages.error(request, "No se proporcionó un ID de receta válido.")
        
        # Si no es válido, muestra el formulario de nuevo con los mensajes de error
        return render(request, self.template_name, {'form': form, 'receta': receta})


class EditarOrdenTrabajoView(SuccessMessageMixin, generic.UpdateView):
    model = OrdenTrabajo
    fields = (
    'fechaEntregaOrdenTrabajo',
    'horaEntregaOrdenTrabajo',
    'laboratorioLejos',
    'gradoLejosOd',
    'gradoLejosOi',
    'prismaLejosOd',
    'prismaLejosOi',
    'tipoCristalLejos',
    'colorCristalLejos',
    'adicionLejosOd',
    'adicionLejosOi',
    'marcoLejos',
    'valorMarcoLejos', 
    'valorCristalesLejos',
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
    'tipoPago',
    'numeroVoucherOrdenTrabajo',
    'observacionOrdenTrabajo'
    )
    success_url = reverse_lazy('ordenTrabajo_list')
    success_message = "La Orden de Trabajo se ha editado exitosamente."

def get_initial(self):
        initial = super().get_initial()
        initial['numeroOrdenTrabajo'] = self.object.numeroOrdenTrabajo  # Valor del modelo
        return initial

def form_valid(self, form):
        # Aquí puedes agregar lógica si necesitas procesar el formulario
        return super().form_valid(form) 
class EliminarOrdenTrabajoView(SuccessMessageMixin, generic.DeleteView):
    model = OrdenTrabajo
    # template_name = 'ordenTrabajo_delete'
    success_url = reverse_lazy('ordenTrabajo_list')
    success_message = "La Orden de Trabajo se ha eliminado exitosamente."

# Usuarios
class UsuarioListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = CustomUser
    template_name = 'optica/usuario_list.html'
    context_object_name = 'usuarios'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')  # Ordenar por 'id' o cualquier otro campo relevante
        query = self.request.GET.get('q')
        if query:
            user_type_map = {
                'Administrador': 1,
                'Atendedor': 2,
                'Técnico': 3
            }
            user_type_value = user_type_map.get(query, None)
            if user_type_value is not None:
                queryset = queryset.filter(user_type=user_type_value)
            else:
                queryset = queryset.filter(
                    Q(username__icontains=query) |
                    Q(email__icontains=query) |
                    Q(first_name__icontains=query) |
                    Q(ap_paterno__icontains=query) |
                    Q(ap_materno__icontains=query) |
                    Q(rut__icontains=query)
                )
        return queryset

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type in [1, 2, 3]  # Administrador y Atendedor

class UsuarioCreateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'optica/usuario_form.html'
    success_url = reverse_lazy('usuario_list')
    success_message = "Usuario {username} creado con éxito."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Crear Usuario'
        context['is_edit'] = False
        return context

    def form_valid(self, form):
        form.instance.username = form.cleaned_data['username']
        self.object = form.save()
        password = form.cleaned_data.get('password1')
        send_user_creation_email(self.object, password)
        # Limpiar los mensajes de error antes de agregar el mensaje de éxito
        storage = messages.get_messages(self.request)
        list(storage)  # Consume todos los mensajes para limpiarlos
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message.format(username=self.object.username)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 1  # Solo Administrador
    

class UsuarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'optica/usuario_form.html'
    success_url = reverse_lazy('usuario_list')
    success_message = "Usuario {username} actualizado con éxito."

    def get_success_message(self, cleaned_data):
        return self.success_message.format(username=self.object.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Editar Usuario'
        context['is_edit'] = True
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 1  # Solo Administrador

class UsuarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = CustomUser
    template_name = 'optica/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')
    success_message = "Usuario borrado con éxito."

    #Nuevo
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 1  # Solo Administrador