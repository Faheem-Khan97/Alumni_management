from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogPage, name = 'blog-home' ),
    path('createBlog/', views.createBlog, name = 'createBlog' ),

]