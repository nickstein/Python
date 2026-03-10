from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

#UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


#Update form
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']