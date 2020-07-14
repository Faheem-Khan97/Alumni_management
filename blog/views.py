from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, BlogPostWithFilesForm, CommentForm, EventCreationForm

from .models import BlogPost, Files_Of_posts, Comment,Event
# Create your views here.


@login_required(login_url = 'loginPage')
def blogPage(request):

    posts = BlogPost.objects.all().order_by('-last_modified')


    paginator = Paginator(posts, 3)
    num_of_pages = paginator.num_pages
    page = request.GET.get('page') # page number
    print(page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        print(page)

        posts = paginator.page(page) # page object, containes posts of a specific page
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #print(posts)
    print(page)
    return render(request, 'blog/blog-home.html', { 'page': page, 'posts': posts , 'num_of_pages':num_of_pages})


def OneBlog(request,pk):
    post = BlogPost.objects.get(id= pk)
    comments = post.comment_set.all()


    print(comments)
    NoOfComments = comments.count()

    print(NoOfComments)

    form = CommentForm()
    if request.method == 'POST':
        print('Hi')
        form = CommentForm(request.POST)
        if form.is_valid():
            commentBy = request.user
            comment = form.cleaned_data.get('comment')
            Comment.objects.create(comment_by = commentBy, blogpost =post, comment = comment )
            return redirect(reverse('OneBlog', kwargs={"pk": pk}))



    return render(request, 'blog/OneBlogPage.html', {'post': post , 'form':form, 'comments':comments, 'NoOfComments': NoOfComments})


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



def eventList(request):

    Events = Event.objects.all().order_by('-event_date')

    return render(request, 'blog/Eventlist.html', {'eventList':Events})



def createEvent(request):
  
    form = EventCreationForm

    if request.method == 'POST':

        form = EventCreationForm(request.POST)
        if form.is_valid():
            Event =  form.save(commit = False)
            Event.created_by = request.user
            Event.save()
            return redirect('eventList')

    context = {'form':form}
    return render(request, 'blog/EventCreation.html', context)


def deleteEvent(request, pk):
    event = Event.objects.get(id = pk)
    if request.method == 'POST':
        event.delete()
        return redirect('eventList')



    return render(request, 'blog/deleteEvent.html', {'event':event})

def updateEvent(request, pk):

    oneEvent = Event.objects.get(id= pk)
    form = EventCreationForm(instance = oneEvent)

    if request.method == 'POST':

        form = EventCreationForm(request.POST, instance = oneEvent)
        if form.is_valid():
            oneEvent =  form.save(commit = False)
            
            oneEvent.save()
            return redirect('eventList')
   

    return render(request, 'blog/updateEvent.html', {'form':form})
