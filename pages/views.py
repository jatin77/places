from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment
from django.shortcuts import redirect

def index(request):
    posts=Post.objects.all() 
    context={
        'posts':posts
    }
    return render(request,'pages/index.html',context)

def posts(request):
    posts=Post.objects.all() 
    context={
        'posts':posts
    }
    return render(request,'pages/posts.html',context)

def post(request,post_id):
    
    post=Post.objects.get(pk=post_id)
    comments=Comment.objects.filter(on_post=post)
    context={
        'post':post,
        'comments':comments
    }
    return render(request,'pages/post.html',context)


def addPostPage(request):
    if request.user.is_authenticated:
        current_user = request.user
        return render(request,'pages/add-post.html')
    else:
        return redirect('index')
    # Do something for anonymous users.
