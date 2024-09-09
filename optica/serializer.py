from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'