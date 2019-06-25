from django.db import models
from django.utils.timezone import now

# Creando modelo de ofertas
class Post(models.Model):
    title=models.CharField(max_length=200,verbose_name="Título")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de publicación",default=now)
    image=models.ImageField(verbose_name="Imagen",upload_to="blog",null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=["-created"]
    
    def _str_(self):
        return self.title
