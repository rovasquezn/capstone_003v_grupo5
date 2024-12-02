from django import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

# Importaciones de rest_framework
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

# Importaciones de vistas personalizadas
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
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
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(
        template_name='optica/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='optica/password_reset_complete.html'
    ), name='password_reset_complete'),

    path('usuarios/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/create/', views.UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/update/', views.UsuarioUpdateView.as_view(), name='usuario_edit'),
    path('usuarios/<int:pk>/delete/', views.UsuarioDeleteView.as_view(), name='usuario_delete'),

    path('mi_perfil/', views.mi_perfil, name='mi_perfil'),

    path('cliente_list/', views.ListarClienteView.as_view(), name='cliente_list'),
    path('cliente_new/', views.CrearClienteView.as_view(), name='cliente_new'),    
    path('<int:pk>/cliente_edit/', views.EditarClienteView.as_view(), name='cliente_edit'),
    path('<int:pk>/cliente_delete/', views.EliminarClienteView.as_view(), name='cliente_delete'),
    
    path('receta_list', views.ListarRecetaView.as_view(), name='receta_list'),
    path('receta_new/', views.CrearRecetaView.as_view(), name='receta_new'),    
    path('<int:pk>/receta_edit/', views.EditarRecetaView.as_view(), name='receta_edit'),
    path('<int:pk>/receta_delete/', views.EliminarRecetaView.as_view(), name='receta_delete'),
    
    path('ordenTrabajo_list', views.ListarOrdenTrabajoView.as_view(), name='ordenTrabajo_list'),
    path('ordenTrabajo_new/', views.CrearOrdenTrabajoView.as_view(), name='ordenTrabajo_new'),    
    path('<int:pk>/ordenTrabajo_edit/', views.EditarOrdenTrabajoView.as_view(), name='ordenTrabajo_edit'),
    path('<int:pk>/ordenTrabajo_delete/', views.EliminarOrdenTrabajoView.as_view(), name='ordenTrabajo_delete'),
    
    path('abono/new/', views.CrearAbonoView.as_view(), name='abono_new'),
    
    path('abono_list', views.ListarAbonoView.as_view(), name='abono_list'),
    path('abono_new/', views.CrearAbonoView.as_view(), name='abono_new'),    
    path('<int:pk>/abono_edit/', views.EditarAbonoView.as_view(), name='abono_edit'),
    path('<int:pk>/abono_delete/', views.EliminarAbonoView.as_view(), name='abono_delete'),

    # path('certificado_list', views.ListarCertificadoView.as_view(), name='certificado_list'),
    path('certificado_new/', views.CrearCertificadoView.as_view(), name='certificado_new'),    
    path('certificado_send/', views.enviar_certificado_pdf, name='enviar_certificado_pdf'),
    # path('<int:pk>/certificado_edit/', views.EditarCertificadoView.as_view(), name='certificado_edit'),
    # path('<int:pk>/certificado_delete/', views.EliminarCertificadoView.as_view(), name='certificado_delete'),
    # path('certificado/new/', views.CrearCertificadoView.as_view(), name='certificado_new'),
    path('certificado/generar/', views.generar_certificado, name='generar_certificado'),
    path('certificado/pdf/<int:pk>/', views.CertificadoPdfView.as_view(), name='certificado_download'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)