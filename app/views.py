from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm, TodoForm
from .models import Todo
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = request.user
        
        if request.method == 'POST':        
            form = TodoForm(request.POST)
            
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                messages.success(request, 'Todo added successfully.')
                return redirect('home')
        else:
            form = TodoForm()
            
        todos = Todo.objects.filter(user=user).order_by("-priority")
        return render(request, 'app/home.html', {'form': form, 'todos': todos})
    else:
        messages.error(request, "You must login to view your todos.")
        return redirect('login')

def change_status(request, pk, status):
    todo = Todo.objects.get(pk=pk)
    todo.status = status
    todo.save()
    messages.info(request, 'Status updated successfully.')
    return redirect('home')

def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    messages.info(request, 'Todo deleted successfully.')
    return redirect('home')
  

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data.get("username")
                upass = form.cleaned_data.get("password")
                
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'You logged in as {request.user}.')
                    return redirect('home')
        
        else:
            form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    else:
        messages.warning(request, 'You are already logged in.')
        return redirect('home')

def signup_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully.')
                return redirect('login')
        else:
            form = SignUpForm()   

        return render(request, 'account/signup.html', {'form': form})
    else:
        messages.warning(request, 'You are already logged in.')
        return redirect('home')

def edit_details(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST, instance=User.objects.get(pk=pk))
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('home')
        else:
            form = SignUpForm(instance=User.objects.get(pk=pk))   

        return render(request, 'account/edit_details.html', {'form': form})
    else:
        messages.warning(request, 'You have to login first.')
        return redirect('login')
    

def logout_user(request):
    logout(request)
    messages.error(request, 'You have been logged out.')
    return redirect('login')