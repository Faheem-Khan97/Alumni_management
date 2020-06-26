from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogPage, name = 'blog-home' ),
    path('createBlog/', views.createBlog, name = 'createBlog' ),
    path('updateBlog/<int:pk>', views.updateBlog, name = 'updateBlog'),
    path('deleteBlog/<int:pk>', views.deleteBlog, name = 'deleteBlog'),

    path('deleteFile/<int:pk>', views.deleteFile, name = 'deleteFile'),
    path('OneBlog/<int:pk>', views.OneBlog, name = 'OneBlog'),



    

]