from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, BlogPostWithFilesForm

from .models import BlogPost, Files_Of_posts
# Create your views here.


@login_required(login_url = 'loginPage')
def blogPage(request):

    posts = BlogPost.objects.all()
    return render(request, 'blog/blog-home.html', {'posts': posts})




@login_required(login_url = 'loginPage')
def createBlog(request):

    blogForm = BlogPostWithFilesForm()

    if request.method == 'POST':

        form =  BlogPostWithFilesForm(request.POST or None, request.FILES or None)
        if request.FILES is not None:
            files = request.FILES.getlist('files')

        if form.is_valid():

            user = request.user
            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            blog_obj = BlogPost.objects.create(author = user, title = title, body = body )

            for f in files:
                Files_Of_posts.objects.create(blogpost = blog_obj, files = f)

        return redirect('blog-home')

    return render(request,'blog/write-blog.html', {'form': blogForm})



