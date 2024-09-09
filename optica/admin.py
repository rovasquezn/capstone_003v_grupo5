from django.contrib import admin
from .models import Cliente
from .models import Atendedor
from .models import Tecnico
from .models import Receta
from .models import Abono
from .models import OrdenTrabajo
from .models import Certificado
from .models import Administrador


# Register your models here.

admin.site.register(Cliente)
admin.site.register(Atendedor)
admin.site.register(Tecnico)
admin.site.register(Receta)
admin.site.register(Abono)
admin.site.register(OrdenTrabajo)
admin.site.register(Certificado)
admin.site.register(Administrador)


