from rest_framework import viewsets
from .serializer import ClienteSerializer
from .serializer import RecetaSerializer
from .models import Cliente, Receta

from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views import generic
from django.db.models import QuerySet
from django.db.models import Q

from .forms import RecetaForm 
from django.views import View

# from .serializer import AtendedorSerializer
# from .serializer import TecnicoSerializer
# from .serializer import RecetaSerializer
# from .serializer import AbonoSerializer
# from .serializer import OrdenTrabajoSerializer
# from .serializer import CertificadoSerializer
# from .serializer import AdministradorSerializer

# from .models import Atendedor
# from .models import Tecnico
# from .models import Receta
# from .models import Abono
# from .models import OrdenTrabajo
# from .models import Certificado
# from .models import Administrador

# Create your views here.
class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


# class AtendedorView(viewsets.ModelViewSet):
#     serializer_class = AtendedorSerializer
#     queryset = Atendedor.objects.all()


# class TecnicoView(viewsets.ModelViewSet):
#     serializer_class = TecnicoSerializer
#     queryset = Tecnico.objects.all()


class RecetaView(viewsets.ModelViewSet):
    serializer_class = RecetaSerializer
    queryset = Receta.objects.all()


# class AbonoView(viewsets.ModelViewSet):
#     serializer_class = AbonoSerializer
#     queryset = Abono.objects.all()


# class OrdenTrabajoView(viewsets.ModelViewSet):
#     serializer_class = OrdenTrabajoSerializer
#     queryset = OrdenTrabajo.objects.all()


# class CertificadoView(viewsets.ModelViewSet):
#     serializer_class = CertificadoSerializer
#     queryset = Certificado.objects.all()


# class AdministradorView(viewsets.ModelViewSet):
#     serializer_class = AdministradorSerializer
#     queryset = Administrador.objects.all()






# Create your views here.
class ListarClienteView(generic.ListView):
    model = Cliente
    paginate_by = 8

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return Cliente.objects.filter(
                Q(nombreCliente__icontains=q) | Q(apPaternoCliente__icontains=q)| Q(rutCliente__icontains=q))
        
        return super().get_queryset()
    

class CrearClienteView(generic.CreateView):
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



class EditarClienteView(generic.UpdateView):
    model = Cliente
    fields = ('nombreCliente',
    'apPaternoCliente',
    'apMaternoCliente', 
    'celularCliente',
    'telefonoCliente', 
    'emailCliente',
    'direccionCliente',)
    success_url = reverse_lazy('cliente_list')


class EliminarClienteView(generic.DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')


class ListarRecetaView(generic.ListView):
    model = Receta
    paginate_by = 8
    
    def get_queryset(self) -> QuerySet[Any]: 
        q = self.request.GET.get('q')
        if q:
            return Receta.objects.filter(
                Q(rutCliente__nombreCliente__icontains=q) | 
                Q(rutCliente__rutCliente__icontains=q)
            )
        return super().get_queryset()
    

class CrearRecetaView(generic.CreateView):
    
    model = Receta
    fields = ('idReceta',
    'rutCliente',
    'dvRutCliente',
    'nombreCliente',
    'apPaternoCliente',
    'apMaternoCliente',
    'celularCliente',
    'telefonoCliente',
    'numeroReceta', 
    'fechaReceta', 
    'lejosOd',
    'lejosOi',
    'cercaOd', 
    'cercaOi',
    'dpCerca', 
    'dpLejos',
    'tipoLente',
    'institucion',
    'doctorOftalmologo',
    'observacionReceta')
    success_url = reverse_lazy('receta_list')
    
    # def __init__(self, *args, **kwargs):
    #     super(RecetaForm, self).__init__(*args, **kwargs)
        
    #     # Bloquear los campos para que sean solo lectura
    #     self.fields['rutCliente'].widget.attrs['readonly'] = True
    #     self.fields['dvRutCliente'].widget.attrs['readonly'] = True
    #     self.fields['nombreCliente'].widget.attrs['readonly'] = True
    #     self.fields['apPaternoCliente'].widget.attrs['readonly'] = True
    #     self.fields['apMaternoCliente'].widget.attrs['readonly'] = True
    #     self.fields['celularCliente'].widget.attrs['readonly'] = True
    #     self.fields['telefonoCliente'].widget.attrs['readonly'] = True
        


    template_name = 'optica/receta_form.html'  # Cambia esto al nombre de tu template
    
    def get(self, request):
        cliente = None
        rut_cliente = request.GET.get('rut_cliente')
        
        # Buscar cliente por RUT
        if rut_cliente:
            try:
                cliente = Cliente.objects.get(rutCliente=rut_cliente)
            except Cliente.DoesNotExist:
                cliente = None
        
        # Cargar formulario de receta, si existe cliente, se pueden prellenar campos
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
        form = RecetaForm(request.POST)
        
        if form.is_valid():
            form.save()  # Guardar la receta
            return redirect('receta_list')  # Redirige a la lista de recetas
        
        return render(request, self.template_name, {'form': form})




class EditarRecetaView(generic.UpdateView):
    model = Receta
    fields = ('numeroReceta', 
    'fechaReceta', 
    'lejosOd',
    'lejosOi',
    'cercaOd', 
    'cercaOi',
    'dpCerca', 
    'dpLejos',
    'tipoLente',
    'institucion',
    'doctorOftalmologo',)
    success_url = reverse_lazy('receta_list')


class EliminarRecetaView(generic.DeleteView):
    model = Receta
    success_url = reverse_lazy('receta_list')
