from rest_framework import serializers
from .models import Cliente
from .models import Atendedor
from .models import Tecnico
from .models import Receta
from .models import Abono
from .models import OrdenTrabajo
from .models import Certificado
from .models import Administrador


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'


# class AtendedorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Atendedor
#         # fields = ('id', 'title', 'description', 'done')
#         fields = '__all__'


# class TecnicoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tecnico
#         # fields = ('id', 'title', 'description', 'done')
#         fields = '__all__'


class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'


# class AbonoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Abono
#         # fields = ('id', 'title', 'description', 'done')
#         fields = '__all__'


# class OrdenTrabajoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrdenTrabajo
#         # fields = ('id', 'title', 'description', 'done')
#         fields = '__all__'


# class CertificadoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Certificado
#         # fields = ('id', 'title', 'description', 'done')
#         fields = '__all__'


# class AdministradorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Administrador
#         # fields = ('id', 'title', 'description', 'done')
#         fields = '__all__'