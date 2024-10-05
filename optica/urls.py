from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from optica import views

router = routers.DefaultRouter()
#router.register(r'cliente', views.ClienteView, 'Cliente')
# router.register(r'atendedor', views.AtendedorView, 'Atendedor')
# router.register(r'tecnico', views.TecnicoView, 'Tecnico')
# router.register(r'receta', views.RecetaView, 'Receta')
# router.register(r'abono', views.AbonoView, 'Abono')
# router.register(r'ordentrabajo', views.OrdenTrabajoView, 'Orden de Trabajo')
# router.register(r'certificado', views.CertificadoView, 'Certificado')
# router.register(r'administrador', views.AdministradorView, 'Administrador')


urlpatterns = [
    #path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Optica API')),

    path('', views.ListarClienteView.as_view(), name='cliente_list'),
    path('cliente_new/', views.CrearClienteView.as_view(), name='cliente_new'),    
    path('<int:pk>/cliente_edit/', views.EditarClienteView.as_view(), name='cliente_edit'),
    path('<int:pk>/cliente_delete/', views.EliminarClienteView.as_view(), name='cliente_delete'),
    
    
    path('receta_list', views.ListarRecetaView.as_view(), name='receta_list'),
    path('receta_new/', views.CrearRecetaView.as_view(), name='receta_new'),    
    path('<int:pk>/receta_edit/', views.EditarRecetaView.as_view(), name='receta_edit'),
    path('<int:pk>/receta_delete/', views.EliminarRecetaView.as_view(), name='receta_delete'),
    
]