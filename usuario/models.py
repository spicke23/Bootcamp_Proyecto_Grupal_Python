
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk} )

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class SubCategoria(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    rut=models.CharField(max_length=10, primary_key=True)
    nombre=models.CharField(max_length=50)
    personacontacto=models.CharField('Persona Contacto',max_length=50)
    telefono=models.CharField('Teléfono', max_length=12)
    region=models.CharField('Región',max_length=200)
    comuna=models.CharField(max_length=200)
    direccion=models.CharField('Dirección',max_length=200)
    categoria=models.ForeignKey(Categoria,null=True, on_delete=models.SET_NULL)
    subcategoria=models.ForeignKey(SubCategoria, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre