from itertools import product
from django import forms
from django.db.models import fields
from .models import Producto




class ProductosForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=("sku","nombre","proveedor","cantidad","precio","imagen")



        