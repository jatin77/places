from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import auth, messages

def signin(request):
    return render(request, 'auth/signin.html')

def signup(request):
    return render(request, 'auth/signup.html')

def signinuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials.')
            return redirect('signin')


def signoutuser(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')


def signupuser(request):
    if request.method=='POST':
        # Get Values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        # Check if passwords match
        if password1==password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request,"The username already exist's")
                return redirect('signup')
            else:
                # Check Email
                if User.objects.filter(email=email).exists():
                    messages.error(request,"The email already exist's")
                    return redirect('signup')
                else:
                    # Looks Good
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name= last_name)
                    # Send to login page
                    user.save()
                    messages.success(request,'You are now a registered user.')
                    return redirect('signin')
        else:
            messages.error(request,"The two password's don't match")
            return redirect('signup')
    else:
        return render(request,'auth/signup.html')



