from django.urls import path
from . import views
from .views import meus_posts

app_name = 'forum_view'  # Esta linha é essencial para definir o namespace

urlpatterns = [
    path('', views.forum, name='forum'),
    path('forumOne/<int:pk>/', views.forumOne, name='forum_one'),
    path('forumOne/<int:post_id>/like/', views.like_post, name='like_post'),
    path('formulario/', views.criar_post, name='criar_post'),
    path('meus-posts/', meus_posts, name='meus_posts'),
]
