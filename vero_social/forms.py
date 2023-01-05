from django import forms
from .models import Post_vero
from logging import PlaceHolder
from tkinter.tix import IMAGE
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from tkinter import Place, messagebox



class PostForm(forms.ModelForm):    
    class Meta:
        model = Post_vero
        fields = ('body', 'image', 'tag')
