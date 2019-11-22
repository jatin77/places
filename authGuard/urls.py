from . import views
from django.urls import path

urlpatterns = [
    path('auth/signup/', views.signup, name='signup'),
    path('auth/signin/', views.signin, name='signin'),
    path('auth/signin/user/', views.signinuser, name='signinuser'),
    path('auth/signup/user/', views.signupuser, name='signupuser'),
    path('auth/signout/',views.signoutuser,name='signoutuser'),
]