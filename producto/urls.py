from django.urls import path
from . import views

urlpatterns=[
    path('nuevoproducto/', views.nuevoproducto, name="producto-nuevo"),
    path('productos/', views.listarPro, name="producto-listado")
    
    ]