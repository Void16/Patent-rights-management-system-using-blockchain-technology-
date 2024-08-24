""" from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    ethereum_address = forms.CharField(max_length=42)
    private_key = forms.CharField(max_length=64)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'ethereum_address', 'private_key']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email') """

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
""" class UserRegisterForm(UserCreationForm):
    ethereum_address = forms.CharField(max_length=42, help_text="Enter your Ethereum address (42 characters long).")
    private_key = forms.CharField(max_length=64, widget=forms.PasswordInput, help_text="Enter your private key (64 characters long).")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'ethereum_address', 'private_key'] """
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


""" class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email') """

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
