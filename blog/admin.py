from django.contrib import admin
from .models import BlogPost,Files_Of_posts, Comment, Event
# Register your models here.


admin.site.register(BlogPost)
admin.site.register(Files_Of_posts)
admin.site.register(Comment)
admin.site.register(Event)


