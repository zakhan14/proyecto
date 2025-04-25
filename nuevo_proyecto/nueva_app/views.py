from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistroForm, LoginForm, PostForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Tag, Comment
from django.urls import reverse_lazy, reverse



# vistas genericas para trabajar CRUD

class PostListView(ListView):
    model = Post
    template_name= "post_list.html"

class PostDetailView(FormMixin,DetailView):
    model = Post
    template_name = "post_detail.html"
    form_class= CommentForm
   
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs) 
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post =self.object
        comment.save()

        return redirect(self.get_success_url())

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_create.html"
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        

        tag_string = form.cleaned_data.get('tag_string', '')
        if tag_string:
            tag_names =[t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                exists= Tag.objects.filter(name__iexact=name).exists()
                if not exists:
                    new_tag =Tag.objects.create(name=name)
                    post.tags.add(new_tag)
                else:
                    existing_tag = Tag.objects.get(name__iexact=name)
                    post.tags.add(existing_tag)

        return super().form_valid(form)

class PostUpdateView (UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()

        tag_string = form.cleaned_data.get('tag_string', '')
        if tag_string:
            tag_names =[t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                exists= Tag.objects.filter(name__iexact=name).exists()
                if not exists:
                    new_tag =Tag.objects.create(name=name)
                    post.tags.add(new_tag)
                else:
                    existing_tag = Tag.objects.get(name__iexact=name)
                    post.tags.add(existing_tag)

        return super().form_valid(form)

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
            remember= request.POST.get('remember_me')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Correo no Registrado")
                return redirect('login')
            
            user_auth= authenticate(request, username=user.username, password=password)

            if user_auth is not None:
                login(request, user_auth)

                if not remember: 
                    request.session.set_expiry(0)


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
def politica_cookies(request):
    return render (request, 'politica_cookies.html') 
