from django import forms
from django.db.models import fields
from .models import  Proveedor



class UserForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)


# class FormUsuario(forms.ModelForm):
#     class Meta:
#         model=Usuario
#         fields=('rut','nombre','apellido','edad')

class FormProveedor(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=('rut','nombre','personacontacto','telefono','region','comuna','direccion')

