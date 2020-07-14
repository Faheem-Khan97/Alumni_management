from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class BlogPost(models.Model):
    author  = models.ForeignKey(User, on_delete = models.CASCADE)
    title  = models.CharField(max_length = 160, null = True, blank = True)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


    def __str__(self):
        return str(self.author)


class Files_Of_posts(models.Model):

    blogpost = models.ForeignKey(BlogPost, on_delete = models.CASCADE)
    files = models.FileField(null = True, blank = True)

    def __str__(self):
        return str(self.blogpost.id)


class Comment(models.Model):
    comment_by = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete = models.CASCADE)
    comment = models.CharField(blank = True, null = True , max_length = 180 )

    
    def __str__(self):
        return str(self.blogpost.id)

    
class Event(models.Model):
    created_by  = models.ForeignKey(User, on_delete = models.CASCADE)
    event_name = models.CharField(max_length = 100, null = True)
    event_details = models.TextField(blank = True, null= True)
    venue = models.CharField(max_length = 120, null = True)
    event_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add = True)
    last_edited = models.DateTimeField(auto_now = True)



    def __str__(self):
        return str(self.event_name)