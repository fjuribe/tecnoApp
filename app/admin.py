from django.contrib import admin
from .models import Marca,Producto,Contacto_ya
from .forms import ProductoFormulario
# Register your models here.

# class ProductoAdmin(admin.ModelAdmin):
# 	list_display=['nombre','precio','descripcion','nuevo','marca','fecha_fabricacion']
# 	list_editable=['precio']
# 	list_per_page=10


class Contacto_yaAdmin(admin.ModelAdmin):
	list_display=['nombre','correo','tipo_consulta','mensaje','avisos']
	list_per_page=10

class ProductoAdmin(admin.ModelAdmin):
	list_display=['nombre','precio','descripcion','nuevo','marca','fecha_fabricacion']
	list_per_page=10
	form=ProductoFormulario

admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Contacto_ya,Contacto_yaAdmin)