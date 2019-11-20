from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/',views.posts, name="posts"),
    path('post/<int:post_id>/', views.post, name='post'),
    path('add-post/',views.addPostPage, name='add-post')
]
