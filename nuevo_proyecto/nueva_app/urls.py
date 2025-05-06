from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from .views import TagListView, TagCreateView, TagDeleteView, PostbyTagView  # Importación corregida

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('mipag/', views.mipag, name='mipag'),
    path('ppt/', views.ppt, name='ppt'),
    path('registro/', views.registroView, name='registro'),
    path('logout/', views.logoutView, name='logout'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/newtag/', TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag_delete'),
    path('post_by_tag/<int:pk>/', PostbyTagView.as_view(), name='post_list_by_tag'),  # URL corregida
    path('politica-cookies/', views.politica_cookies, name='politica_cookies'),
    path('tags/<int:pk>/posts/', PostbyTagView.as_view(), name='post_by_tag'),
    path('weather/', views.weather,  name='weather'),
    path('exchange/', views.exchange,  name='exchange'),

]
