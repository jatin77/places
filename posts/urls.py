from . import views
from django.urls import path


urlpatterns = [
    path('add-post/new-post/',views.newPostAdded, name='newPostAdded')
]
