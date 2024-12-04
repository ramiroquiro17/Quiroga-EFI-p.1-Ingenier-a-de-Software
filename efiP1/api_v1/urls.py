from rest_framework.routers import DefaultRouter, path

from api_v1.views.concesionaria import AutoViewSet, ComentariosPorAuto, SedeViewSet, ProveedorViewSet, UserViewSet

router = DefaultRouter()
router.register(r'autos',AutoViewSet,'autos')
router.register(r'sedes',SedeViewSet,'sedes')
router.register(r'proveedores',ProveedorViewSet,'proveedores')
router.register(r'users',UserViewSet,'users')

urlpatterns = [
    path('autos/<int:auto_id>/comentarios/', ComentariosPorAuto.as_view(), name='comentarios-por-auto'),
]

urlpatterns += router.urls