from django.contrib import admin
from .models import Proveedor,Categoria,SubCategoria,Post
# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Post)