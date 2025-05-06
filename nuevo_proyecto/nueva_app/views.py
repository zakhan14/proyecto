from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistroForm, LoginForm, PostForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Tag, Comment
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


#Imports para API de terceros y Cache
import requests
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.conf import settings


# vistas genericas para trabajar CRUD

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    form_class = CommentForm
   
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
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
        comment.post = self.object
        comment.save()

        return redirect(self.get_success_url())

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # ✅ CORRECTO
    template_name = "post_create.html"
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        # Guardamos el post, pero aún no le asignamos el id
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()  # Aquí le damos un id al post al guardarlo en la base de datos

        # Luego de guardar el post, añadimos los tags
        tag_string = self.request.POST.get('tag_string', '')
        if tag_string:
            tag_names = [t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name__iexact=name, defaults={'name': name})
                post.tags.add(tag)  # Añadimos el tag al post

        return super().form_valid(form)


class PostUpdateView(UpdateView):
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
            tag_names = [t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                exists = Tag.objects.filter(name__iexact=name).exists()
                if not exists:
                    new_tag = Tag.objects.create(name=name)
                    post.tags.add(new_tag)
                else:
                    existing_tag = Tag.objects.get(name__iexact=name)
                    post.tags.add(existing_tag)

        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

class PostByTagView(ListView):
    model = Post
    template_name = 'post_list_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Obtener el tag por su pk
        tag = Tag.objects.get(id=self.kwargs['pk'])
        # Filtrar los posts que tienen ese tag
        return Post.objects.filter(tags=tag)


# Vistas para gestionar Tag
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

# views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Tag

class PostbyTagView(ListView):
    model = Post
    template_name = 'post_list_by_tag.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        tag = Tag.objects.get(id=self.kwargs['pk'])
        return Post.objects.filter(tags=tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(id=self.kwargs['pk'])
        context['tag'] = tag
        return context

# Vistas de login, registro y logout
def home(request):
    return render(request, 'home.html')

def mipag(request):
    return render(request, 'mipag.html')

def ppt(request):
    return render(request, 'ppt.html')

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember = request.POST.get('remember_me')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Correo no registrado")
                return redirect('login')

            user_auth = authenticate(request, username=user.username, password=password)

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
    messages.info(request, "Has cerrado sesión. ¡Vuelve pronto!")
    return redirect('home')

def politica_cookies(request):
    return render(request, 'politica_cookies.html')


#Vista para API de terceros EXCHANGE

#@cache_page(60*30) # 1800s
def weather (request):
    city= request.GET.get('city', 'Santander')
    params = {
        'q' : city,
        'units' : 'metric',
        'appid' : settings.OWN_KEY, 
        'lang' :'es', 
    }
    r = requests.get(
        'https://api.openweathermap.org/data/2.5/weather',
        params=params, timeout=5
    )
    data = r.json()
    respuesta = {
        'city' : data['name'],
        'temp' : data['main']['temp'],
        'icon' : data ['weather'][0]['icon'],
        'desc' : data ['weather'][0]['description'],
    }
    return JsonResponse(respuesta)

#EXCHANGE 


def exchange(request):
    from_currency = request.GET.get('from', 'USD')
    to_currency = request.GET.get('to', 'EUR')
    amount = float(request.GET.get('amount', 100))
    key_EXC = settings.EXCHANGE_KEY
    url = f'https://api.fastforex.io/fetch-all?api_key={key_EXC}'

    try:
        r = requests.get(url, timeout=5)
        data = r.json()

        if 'results' in data and to_currency in data['results']:
            rate = data['results'][to_currency]
            converted = round(rate * amount, 2)
            return JsonResponse({'converted': converted})
        else:
            return JsonResponse({'error': 'Tasa de cambio no encontrada'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
