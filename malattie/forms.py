from .models import Malattia
from django import forms
from logging import PlaceHolder
from tkinter.tix import IMAGE
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from tkinter import Place, messagebox

class PostMalattia(forms.ModelForm):    
    class Meta:
        model = Malattia
        fields = '__all__'
