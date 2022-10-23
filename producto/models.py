
from django.db import models
from usuario.models import Proveedor
# Create your models here.


class Producto(models.Model):
    sku=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=50,null=False)
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    imagen = models.ImageField(upload_to='productos')
    proveedor=models.ForeignKey(Proveedor,null=True, on_delete=models.SET_NULL)


    