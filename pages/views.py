from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib import messages

def index(request):
    posts=Post.objects.order_by('-post_date')[:3]
    posts_count=Post.objects.all()
    context={
        'posts':posts,
        'posts_count':posts_count
    }
    return render(request,'pages/index.html',context)

def posts(request):
    posts_list=Post.objects.order_by('-post_date')
    paginator = Paginator(posts_list, 6)
    page = request.GET.get('page')
    posts=paginator.get_page(page)
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

def addComment(request):
    if request.POST:
        if request.user.is_authenticated:
            comment_content=request.POST['comment']
            if comment_content!= "":
                post_id=request.POST['post_id']
                on_post=Post.objects.get(pk=post_id)
                comment_content=request.POST['comment']
                comment_author=request.user
                comment=Comment(on_post=on_post, comment_content=comment_content, comment_author=comment_author)

                comment.save()
                return redirect('/post/'+post_id+'/')
            else:
                messages.error(request,'Empty fields')
                return redirect('/post/'+post_id+'/')

def liked(request):
    if request.POST:
        post_id=request.POST['post_id']
        post=Post.objects.get(pk=post_id)
        post.post_likes=post.post_likes+1
        post.save()
        return redirect('/post/'+post_id+'/')

def dashboard(request):
    if request.user.is_authenticated:
        user_posts=Post.objects.filter(post_author=request.user)
        context={
            'user_posts':user_posts
        }
        return render(request, 'pages/dashboard.html', context)
    else:
        return redirect('index')
