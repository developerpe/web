from django.urls import path,include
from .views import *

urlpatterns = [
    path('', Home_blog.as_view(), name = 'home_blog'),
    path('prueba/',Prueba, name = "prueba"),
    path('movil/', Blog_movil.as_view(), name = 'blog_movil'),
    path('general/', Blog_general.as_view(), name = 'blog_general'),
    path('tecnologia/', Blog_tecnologia.as_view(), name = 'blog_tecnologia'),
    path('programacion/', Blog_programacion.as_view(), name = 'blog_programacion'),
    path('videojuegos/', Blog_videojuegos.as_view(), name = 'blog_videojuegos'),
    path('tutoriales/', Blog_tutoriales.as_view(), name = 'blog_tutoriales'),
    path('<int:id>/', Detail_Post.as_view(), name = 'detail_post'),
]
