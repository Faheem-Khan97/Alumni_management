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
        return self.title


class Files_Of_posts(models.Model):

    blogpost = models.ForeignKey(BlogPost, on_delete = models.CASCADE)
    files = models.FileField(null = True, blank = True)

    def __str__(self):
        return str(self.blogpost.id)


    def __str__(self):
        return str(self.blogpost.author.email)


