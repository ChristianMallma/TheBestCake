from django.db import models
from django.contrib.auth.models import User

# Creando modelo para subir los diseños
class Design(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    price = models.IntegerField(verbose_name="Precio")

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Catálogo de producto'
        verbose_name_plural = 'Catálogo de productos'
        ordering = ['-created']

    def __str__(self):
        return self.name

class ImagenesProducto(models.Model):
    descripcion = models.CharField(max_length=300)
    producto = models.ForeignKey(Design, related_name="producto_imagenes",on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='catalog')

    def __str__(self):
        return "{}".format(self.producto)
    
class Comentario(models.Model):
    comentario=models.CharField(max_length=400)    
    usuario=models.CharField(max_length=300)
    producto=models.ForeignKey(Design,related_name="producto_comentarios",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return self.comentario

class CarritoCompras(models.Model):  
    usuario=models.ForeignKey(User,related_name="usuario_carrito",on_delete=models.CASCADE)
    producto=models.ForeignKey(Design,related_name="producto_carrito",on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Precio")
    direccion=models.CharField(max_length=400, verbose_name="Dirección",null=True,blank=True)    
    datos_pay=models.CharField(max_length=600, verbose_name="Datos PayPal",null=True,blank=True)    
    comprado=models.BooleanField(default=False,blank=True)
    pendiente=models.BooleanField(default=False,blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return "{} {}".format(self.usuario,self.producto)