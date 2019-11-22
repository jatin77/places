from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/',views.posts, name="posts"),
    path('post/<int:post_id>/', views.post, name='post'),
    path('add-post/',views.addPostPage, name='add-post'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('add-comment/',views.addComment, name='add-comment'),
    path('like/',views.liked, name='liked')
]
