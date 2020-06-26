from django.shortcuts import render, redirect

from django.urls import reverse

from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, BlogPostWithFilesForm

from .models import BlogPost, Files_Of_posts
# Create your views here.


@login_required(login_url = 'loginPage')
def blogPage(request):

    posts = BlogPost.objects.all()
    return render(request, 'blog/blog-home.html', {'posts': posts})


def OneBlog(request,pk):
    post = BlogPost.objects.get(id= pk)

    return render(request, 'blog/OneBlogPage.html', {'post': post})


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

def updateBlog(request, pk):

    post = BlogPost.objects.get(id = pk)
    form = BlogPostWithFilesForm(instance = post)
    old_files = post.files_of_posts_set.all()

    if request.method == 'POST':
        form =  BlogPostWithFilesForm(request.POST or None, request.FILES or None, instance = post)
        if request.FILES is not None:
            files = request.FILES.getlist('files')
           # print(files)

        if form.is_valid():
            post.title = form.cleaned_data.get('title')
            post.body = form.cleaned_data.get('body')
            post.save()

            if files is not None:
                for f in files:
                    print(f)
                    Files_Of_posts.objects.create(blogpost = post, files = f)


        return redirect('blog-home')

    return render(request, 'blog/updateBlog.html', {'form': form, 'post_files':old_files})




def deleteBlog(request, pk):
    post = BlogPost.objects.get(id = pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-home')



    return render(request, 'blog/deletePost.html', {'post':post})




def deleteFile(request,pk):

    postfile = Files_Of_posts.objects.get(id = pk)

    if request.method == 'POST':
        postfile.delete()
        #return redirect('updateBlog/<int:pk>')
        return redirect(reverse('updateBlog', kwargs={"pk": postfile.blogpost.id}))


    return render(request, 'blog/deleteImg.html', {'File':postfile})



