from django import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, CustomPasswordResetView, index, UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, mi_perfil, ListarClienteView, CrearClienteView, EditarClienteView, EliminarClienteView, ListarRecetaView, CrearRecetaView, EditarRecetaView, EliminarRecetaView, ListarOrdenTrabajoView, CrearOrdenTrabajoView, EditarOrdenTrabajoView, EliminarOrdenTrabajoView, CustomPasswordResetConfirmView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/', index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('', RedirectView.as_view(url='/home/', permanent=False)),  # Redirigir la raíz a /home/

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='optica/password_reset.html',
        email_template_name='optica/password_reset_email.html',
        subject_template_name='optica/password_reset_subject.txt',
        html_email_template_name='optica/password_reset_email.html'), 
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='optica/password_reset_done.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(
        template_name='optica/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='optica/password_reset_complete.html'
    ), name='password_reset_complete'),

    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/update/', UsuarioUpdateView.as_view(), name='usuario_edit'),
    path('usuarios/<int:pk>/delete/', UsuarioDeleteView.as_view(), name='usuario_delete'),

    path('mi_perfil/', mi_perfil, name='mi_perfil'),

    path('cliente_list/', ListarClienteView.as_view(), name='cliente_list'),
    path('cliente_new/', CrearClienteView.as_view(), name='cliente_new'),    
    path('<int:pk>/cliente_edit/', EditarClienteView.as_view(), name='cliente_edit'),
    path('<int:pk>/cliente_delete/', EliminarClienteView.as_view(), name='cliente_delete'),

    path('receta_list', ListarRecetaView.as_view(), name='receta_list'),
    path('receta_new/', CrearRecetaView.as_view(), name='receta_new'),    
    path('<int:pk>/receta_edit/', EditarRecetaView.as_view(), name='receta_edit'),
    path('<int:pk>/receta_delete/', EliminarRecetaView.as_view(), name='receta_delete'),

    path('ordenTrabajo_list', ListarOrdenTrabajoView.as_view(), name='ordenTrabajo_list'),
    path('ordenTrabajo_new/', CrearOrdenTrabajoView.as_view(), name='ordenTrabajo_new'),    
    path('<int:pk>/ordenTrabajo_edit/', EditarOrdenTrabajoView.as_view(), name='ordenTrabajo_edit'),
    path('<int:pk>/ordenTrabajo_delete/', EliminarOrdenTrabajoView.as_view(), name='ordenTrabajo_delete'),

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)