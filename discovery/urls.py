from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('pages.urls')),
    path('',include('posts.urls')),
    path('',include('authGuard.urls')),
    path('admin/', admin.site.urls),
]
