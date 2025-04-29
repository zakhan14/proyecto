from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from nueva_app.models import Post, Comment, Tag

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electronico")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electronico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class PostForm(forms.ModelForm):
    tag_string =forms.CharField(required = False, help_text="Separar tags con comas")

    class Meta:
        model = Post
        fields = ['title', 'content']
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()  # Guardamos el post primero
        
        # Ahora procesamos los tags
        tag_string = self.cleaned_data.get('tag_string', '')
        if tag_string:
            # Si hay tags, los procesamos
            tag_names = [t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name__iexact=name)  # Crea el tag si no existe
                post.tags.add(tag)  # Asociamos el tag al post
        
        return post  # Devolvemos el post guardado

class CommentForm(forms.ModelForm):
    content_string = forms.TextInput
    class Meta:
        model = Comment
        fields = ['content']