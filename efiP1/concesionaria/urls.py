from django.urls import path

from concesionaria.views.auto_view import (
    auto_list,
    auto_create,
    auto_delete,
    auto_detail,
    auto_update,
)

from concesionaria.views.sede_view import (
    sede_list,
    sede_create,
    sede_delete,
    sede_detail,
    sede_update,
)

from concesionaria.views.comentario_view import (
    ComentarioDetailView,
    ComentarioCreateView,
    ComentarioView,
    ComentarioDeleteView)

from concesionaria.views.proveedor_view import (
    proveedor_create,
    proveedor_delete,
    proveedor_detail,
    proveedor_list,
    proveedor_update,
)

urlpatterns = [
    path(route='', view=auto_list, name='auto_list'),
    path(route='create/',view=auto_create, name='auto_create'),
    path(route='<int:id>/',view=auto_detail,name="auto_detail"),
    path(route='<int:id>/update/',view=auto_update,name="auto_update"),
    path(route='<int:id>/delete/',view=auto_delete,name="auto_delete"),
    path(route='sede/', view=sede_list, name='sede_list'),
    path(route='sede/create', view=sede_create, name='sede_create'),
    path(route='sede/<int:id>/', view=sede_detail, name='sede_detail'),
    path(route='sede/<int:id>/delete/', view=sede_delete, name='sede_delete'),
    path(route='sede/<int:id>/update/', view=sede_update, name='sede_update'),
    path(route='comentario/', view=ComentarioView.as_view(), name='comentario_list'),
    path(route='comentario/create', view=ComentarioCreateView.as_view(), name='comentario_create'),
    path(route='comentario/<int:id>/', view=ComentarioDetailView.as_view(), name='comentario_detail'),
    path(route='comentario/<int:id>/delete/', view=ComentarioDeleteView.as_view(), name='comentario_delete'),
    path(route='proveedores/', view=proveedor_list, name='proveedor_list'),
    path(route='proveedores/<int:id>/',view=proveedor_detail,name="proveedor_detail"),
    path(route='proveedores/<int:id>/delete/',view=proveedor_delete,name="proveedor_delete"),
    path(route='proveedores/create/',view=proveedor_create, name='proveedor_create'),
    path(route='proveedores/<int:id>/update/',view=proveedor_update,name="proveedor_update"),
    
]