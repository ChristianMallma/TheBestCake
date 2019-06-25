from django.contrib import admin
from .models import Design,Comentario, CarritoCompras, ImagenesProducto

#Extendemos clase de administración
class DesignAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CarritoComprasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ImagenesProductoAdmin(admin.ModelAdmin):
    pass

# Registramos modelo en el administrador
admin.site.register(ImagenesProducto, ImagenesProductoAdmin)
admin.site.register(Design, DesignAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(CarritoCompras, CarritoComprasAdmin)

