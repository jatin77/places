from django.shortcuts import render
from .models import Post
from datetime import datetime
from django.shortcuts import redirect
from django.contrib import messages

def newPostAdded(request): 
    if request.method == 'POST':         
        data=request.POST
        post_content=data.get('post')
        post_author=request.user
        post_likes=0

        post=Post(post_content=post_content, post_author=post_author, post_likes=post_likes)
        if (post_content != ""):
            post.save()
            messages.success(request,'Your post has been added.')
            return redirect('posts')
        else:
            messages.error(request,'Empty field.')
            return redirect('posts')
    return