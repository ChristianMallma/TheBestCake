from django.db import models

# Creando modelo para las páginas secundarias
class Page(models.Model):
    title=models.CharField(verbose_name="Título",max_length=200)
    content=models.TextField(verbose_name="Contenido")
    created=models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated=models.DateTimeField(verbose_name="Fecha de actualización",auto_now=True)

    class Meta:
        verbose_name="página"
        verbose_name_plural="páginas"
        ordering=['title']

    def __str__(self):
        return self.title