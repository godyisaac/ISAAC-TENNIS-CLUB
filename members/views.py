
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from .forms import MemberForm  # for registration
from .models import Member      # your database model
from django.shortcuts import render, redirect
from .forms import CustomLoginForm
from .forms import UserRegisterForm
from django.contrib import messages

def home(request):
    return render(request, 'members/home.html')

def about(request):
    return render(request, 'members/about.html')

def members(request):
    return render(request, 'members/members.html')

def contact(request):
    return render(request, 'members/contact.html')

def join_member(request):
    return render(request, 'members/join.html')

def register_user(request):
    return render(request, 'members/register.html')




def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            # authentication logic same as before
            ...

## Member Registration (for joining)
def join_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You’ve successfully joined as a member!")
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'members/join.html', {'form': form})

# User Registration (for login account)
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Saves user with hashed password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page
    else:
        form = UserRegisterForm()
    return render(request, 'members/register.html', {'form': form})



# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'members/login.html', {'form': form})


# User Logout
def user_logout(request):
    logout(request)
    messages.info(request, "You’ve been logged out successfully.")
    return redirect('login')