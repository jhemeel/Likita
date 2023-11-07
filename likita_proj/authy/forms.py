from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from base.models import User
from django import forms

class MyUserCreationForm(UserCreationForm):
    name = forms.CharField(label="Full Name", 
                           required=True, 
                           widget=forms.TextInput(attrs={'id': 'fname' , 'class': "Fname"}))
    
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'id': "username", 'class': 'Username'}))
    email = forms.EmailField(label = "Email", required=True, help_text="Enter a valid email",
                             widget=forms.EmailInput(attrs={'id': 'mail', 'class': "Email"}))
    
    password1 = forms.CharField(required=True, label="Password", help_text='''Your Password must be at leat 8 alphanumeric characters and 
                                \npassword must not be similar to your username''', widget=forms.PasswordInput(attrs={'id': 'pwd1', 'class': 'Pass1'}))
    password2 = forms.CharField(required=True, label="Retype Password", widget=forms.PasswordInput(attrs={"id": 'pwd2', 'class': "Pass2"}))
    class Meta:
        model = User
        fields = ['name', 'username','email', 'location', 'password1', 'password2']