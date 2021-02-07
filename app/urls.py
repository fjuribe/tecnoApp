from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import eliminar,modificar_producto,home,contacto,galeria,formulario, \
    clientes,alumno,contacto2,galeria2,agregar_producto,listar_productos,registro
urlpatterns = [
    path('', home,name="home"),
    #cliente: con form api
    # path('cliente/',clientes,name="cliente"),


    #alumno
    # path('alumno/',alumno,name="alumno"),

    #contacto: sin form api
    # path('contacto/',formulario,name="contacto"),
    # path('contacto/guardar',contacto,name="formulario"),

    # path('galeria/',galeria,name="galeria"),
    path('contacto/',contacto2,name="contacto2"),
    path('galeria/',galeria2,name="galeria2"),
    path('agregar-producto/',agregar_producto,name="agregar-producto"),
    path('listar-producto/',listar_productos,name="listar-producto"),
    path('modificar-producto/<int:id>/',modificar_producto,name="modificar-producto"),
    path('eliminar-producto/<int:id>/',eliminar,name="eliminar-producto"),
    path('registro/',registro,name="registro"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
