from django.shortcuts import redirect, render
from .forms import ProductosForm
from .models import Producto


def nuevoproducto(request):
    if request.method=="POST":
        form=ProductosForm(request.POST, request.FILES)
        if form.is_valid():
            cliente=form.save(commit=False)
            cliente.save() #se guarda en la db
                  
        return redirect('/productos')

    else:
        form=ProductosForm()
        return render(request,'producto/nuevoproducto.html',{"form":form})


def listarPro(request):
    pro=Producto.objects.all()
    if request.user.is_authenticated:
       
        return render(request,'producto/listadoProductos2admin.html',{"Productos":pro})
        
    else: 
    
        return render(request,'producto/listadoProductos.html',{"Productos":pro})


