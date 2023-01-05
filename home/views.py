from tkinter import *
from tkinter import messagebox
from .models import home_notizia
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import notizia_form

# Create your views here.

def home(request):
    home_notizia_ = home_notizia.objects.all()
    return render(request, 'home\home.html', {'home': home_notizia_})


def inserisci_nuova_notizia(request):
    if request.method == 'POST':
        form = notizia_form(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'home/successo.html')
            return redirect('home')
        else:
            return render(request, 'home/errore.html')
            messagebox.showinfo("Ops!", "Qualcosa è andato storto!", parent=Toplevel(root))


    form = notizia_form()  
    context = {  
        'form':form  
    }  
    
    return render(request, 'home/nuova_notizia.html', context)