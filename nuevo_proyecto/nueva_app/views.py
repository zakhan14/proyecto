from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroForm, LoginForm

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
