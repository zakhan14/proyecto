from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistroForm, LoginForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Tag, Comment
from django.urls import reverse_lazy



# vistas genericas para trabajar CRUD

class PostListView(ListView):
    model = Post
    template_name= "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_create.html"
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView (UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
#vistas para gestionar Tag
class TagListView(ListView):
    model = Tag
    template_name = "tag_list.html"

class TagCreateView(CreateView):
    model = Tag
    fields = ['name']
    template_name = "tag_create.html"
    success_url = reverse_lazy('tag_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tag_confirm_delete.html'
    success_url = reverse_lazy('tag_list')

class PostbyTagView(ListView):
    model = Post
    template_name= "post_list_by_tag.html"



# Create your views here.
def home(request):
    return render (request, 'home.html')
def mipag(request):
    return render (request, 'mipag.html')
def ppt(request):
    return render (request, 'ppt.html')
def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Correo no Registrado")
                return redirect('login')
            user_auth= authenticate(request, username=user.username, password=password)
            if user_auth is not None:
                login(request, user_auth)
                messages.success(request, "¡Has iniciado sesión correctamente!")
                return redirect('mipag')
            else:
                messages.error(request, "¡Contraseña incorrecta!")
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def registroView(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Inicia sesión")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})  

def logoutView(request):
    logout(request)
    messages.info(request, "has cerrado sesión. ¡Vuelve pronto!")
    return redirect('home')
