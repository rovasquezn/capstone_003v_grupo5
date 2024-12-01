from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Cliente, Receta, Abono, OrdenTrabajo, Certificado, CustomUser #, Atendedor, Tecnico, Administrador
from .forms import AdminCustomUserChangeForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.admin.models import LogEntry

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = AdminCustomUserChangeForm
    model = CustomUser
    list_display = ['id','username', 'email', 'first_name', 'ap_paterno', 'ap_materno', 'user_type', 'is_active', 'is_staff']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'ap_paterno', 'ap_materno', 'email', 'rut', 'dv', 'celular')}),
        ('Permisos', {'fields': ('user_type', 'is_active','is_staff')}), #, 'groups', 'user_permissions'
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'ap_paterno', 'ap_materno', 'email', 'rut', 'dv', 'celular', 'user_type', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

    class Media:
        js = (staticfiles_storage.url('bootstrap/js/admin_custom.js'),)

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'object_repr', 'action_flag', 'change_message')
    list_filter = ('action_flag', 'user')
    search_fields = ('object_repr', 'change_message')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cliente)
admin.site.register(Receta)
admin.site.register(Abono)
admin.site.register(OrdenTrabajo)
admin.site.register(Certificado)
admin.site.register(LogEntry, LogEntryAdmin)
""""
admin.site.register(Atendedor)
admin.site.register(Tecnico)
admin.site.register(Administrador)
"""	