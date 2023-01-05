from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Malattia
from .forms import PostMalattia
# Create your views here

def malattie(request):
    if 'q' in request.GET:
        q=request.GET['q']
        Malatti = Malattia.objects.filter(nome_malattia__contains=q)
    else:
        Malatti = Malattia.objects.all()
    return render(request, 'malattie\Malattie.html', {'malattie': Malatti})


def inserisci_nuova_malattia(request):
    if request.method == 'POST':
        form = PostMalattia(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'home/successo.html')
        else:
            return render(request, 'home/errore.html')

    form = PostMalattia()  
    context = {  
        'form':form  
    }  
    
    return render(request, 'malattie/nuova_malattia.html', context)