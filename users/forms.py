from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name','username', 'email', 'subject',)


    
class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'subject',)