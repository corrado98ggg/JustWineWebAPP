from multiprocessing import context
from tkinter import messagebox
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .forms import CustomUserCreationForm
# Create your views here.
# 
# 

def my_view(request):
    if request.method == 'POST':        
        username_ = request.POST.get('username')
        password_ = request.POST.get('password1')
        user = authenticate(request, username=username_, password=password_)
        print(user)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'home/errore.html')
            messagebox.showinfo("Attenzione", "Qualcosa è andato storto riprovare")
    
    form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'registration/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.save()
            messages.success(request, 'Account creato con successo')
            return render(request, 'registration/grazie.html')
        else:
            return render(request, 'home/errore.html')

    form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    
    return render(request, 'registration/signup.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return render(request, 'home/successo.html')
        else:
            return render(request, 'home/errore.html')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'registration/reset_password.html', {
        'form': form
    }) 




def logout_view(request):
    logout(request)
    return redirect('home')
