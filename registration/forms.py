from logging import PlaceHolder
from tkinter.tix import IMAGE
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from tkinter import Place, messagebox


class CustomUserCreationForm(UserCreationForm):  

    username = forms.CharField(label='username', min_length=5, max_length=150, required=True)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput, required=True)  
    password2 = forms.CharField(label='Conferma password', widget=forms.PasswordInput, required=True)  

    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Inserisci il tuo username'
        self.fields['email'].widget.attrs['placeholder'] = 'Inserisci email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Inserisci password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Conferma password'
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():
            messagebox.showinfo("Attenzione", "Esiste già un account con questo username")
            raise ValidationError("User Already Exist")
        return username 

    def clean_email(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.exists():
            messagebox.showinfo("Attenzione", "Esiste già un account con questa email")
            raise ValidationError(" Email Already Exist")  
        return email  

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  

        if password1 and password2 and password1 != password2:
            messagebox.showinfo("Attenzione", "Le due password non corrispondono")
            raise ValidationError("Password don't match")  
        return password2  

    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1'],
        )  
        return user
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
