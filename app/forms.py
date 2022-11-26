from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "status", "priority"]
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        error_messages={'required':"Enter a password"}, 
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        error_messages={'required':"Confirm your password"},
        label="Repeat Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
        error_messages = {
            'username': {
                'required': 'Enter a valid username',
            },
        }
        
        labels= {
            'email': 'Email (Optional)',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        error_messages={'required':"Enter your username"}, 
        label="Username", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    password = forms.CharField(
        error_messages={'required':"Enter your password", 'password_mismatch': "Your Password Mismatch",}, 
        label="Password", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )

    class Meta:
        model = User
        fields = ['username', 'password']
        
