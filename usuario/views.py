
from unicodedata import category
from django.shortcuts import redirect, render
from .forms import LoginForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Proveedor,Categoria,SubCategoria
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView

# Create your views here.



# #creacion de usuario de la app
# def agregarUsuario(request):
#     form=FormUsuario()
#     if request.method=="POST":
#         form=FormUsuario(data=request.POST)
#         usu=form.save(commit=False)#aqui los valore estan en memoria
#         usu.save()
        
#         return redirect('/usuarios/listado')
#     else:
        
#         return render(request,'usuario/createUsuario.html',{"form":form})

#creacion de usuario django
def crearUsuario(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user= User.objects.create_user(nombre,email,password)
            user.save()
        return redirect("/usuarios/listado")

    else:
        form=UserForm()
        return render(request, 'usuario/createuser.html',{'form':form})

def listarUser(request):
   
    usu2=User.objects.all()
    return render(request,'usuario/listarUsuarios.html',{"usu2":usu2})

def login(request):
    if request.method=="POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            
            usu=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request,username=usu,password=clave)
           
            if user is not None:
                auth_login(request,user)
                #return render(request,'usuario/bienvenida.html',{"user":user})
                return redirect("/post")
            else:
                return redirect("/login")
           
    else:
        form=LoginForm()
        return render(request,'usuario/login.html',{"form":form})

@login_required(login_url="/login")
def bienvenido(request):
    return render(request,'usuario/bienvenida.html')

def salir(request):
    logout(request)
    return redirect("/login")


class PostListViews(LoginRequiredMixin,ListView):
    
    login_url = '/login/'
    redirect_field_name = 'login'
    model=Post
    context_object_name = 'posts'
    ordering = ['-fecha_publicacion']
    def get_queryset(self):
        usu=str(self.request.user)
       
        if usu=='telovendo':
            
            return Post.objects.all()
        else:
            
            return Post.objects.filter(autor=self.request.user)

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Post
    fields = ['titulo','comentario']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False

class PostDetailView(DetailView):
    model=Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Post
    fields = ['titulo','comentario']
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'

    model = Post
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True

    success_url='/post'

class ProveedorCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    template_name='usuario/proveedor_form.html'
    model = Proveedor
    fields = ['rut','nombre','personacontacto','telefono','region','comuna','direccion','categoria','subcategoria']
    
    success_url='/proveedor'

class ProveedorListViews(LoginRequiredMixin,ListView):
    
    login_url = '/login/'
    redirect_field_name = 'login'

    template_name='usuario/proveedor_list.html'
    model=Proveedor
    context_object_name = 'proveedores'
   
    


class CategoriaCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    template_name='usuario/categoria_form.html'
    model = Categoria
    fields = ['nombre']
    
    success_url='/categoria'

class CategoriaListViews(LoginRequiredMixin,ListView):
    
    login_url = '/login/'
    redirect_field_name = 'login'

    template_name='usuario/categoria_list.html'
    model=Categoria
    context_object_name = 'categoria'

class SubCategoriaCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    template_name='usuario/subCategoria_form.html'
    model = SubCategoria
    fields = ['nombre','categoria']
    
    success_url='/subcategoria'

class SubCategoriaListViews(LoginRequiredMixin,ListView):
    
    login_url = '/login/'
    redirect_field_name = 'login'

    template_name='usuario/subcategoria_list.html'
    model=SubCategoria
    context_object_name = 'subcategoria'

    
