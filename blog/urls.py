from django.urls import path
from . import views



urlpatterns = [
    path('', views.blogPage, name = 'blog-home' ),
    path('createBlog/', views.createBlog, name = 'createBlog' ),
    path('updateBlog/<int:pk>', views.updateBlog, name = 'updateBlog'),
    path('deleteBlog/<int:pk>', views.deleteBlog, name = 'deleteBlog'),

    path('deleteFile/<int:pk>', views.deleteFile, name = 'deleteFile'),
    path('OneBlog/<int:pk>', views.OneBlog, name = 'OneBlog'),







    path('eventList/', views.eventList, name = 'eventList'),

    path('createEvent/', views.createEvent, name = 'createEvent'),
    path('deleteEvent/<int:pk>', views.deleteEvent, name = 'deleteEvent'),


    path('updateEvent/<int:pk>', views.updateEvent, name = 'updateEvent'),








    

]