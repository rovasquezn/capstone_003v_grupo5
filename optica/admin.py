from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Cliente, Receta, Abono, OrdenTrabajo, Certificado, CustomUser #, Atendedor, Tecnico, Administrador
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.admin.models import LogEntry

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'ap_paterno', 'ap_materno', 'rut', 'dv', 'celular', 'user_type', 'is_staff', 'is_active',)
    list_filter = ('user_type', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'ap_paterno', 'ap_materno', 'email', 'rut', 'dv', 'celular', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'ap_paterno', 'ap_materno', 'rut', 'dv', 'celular', 'user_type', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'first_name', 'ap_paterno', 'ap_materno', 'rut', 'dv', 'celular')
    ordering = ('username',)

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