import tkinter
from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import  Partecipa_vero, forum, Discussione
from .forms import CreateInDiscussion, CretaedInForum, AddPrefe
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model 
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.template.loader import render_to_string


User = get_user_model()


# Create your views here.

def forum_home(request):
    qs = Partecipa_vero.objects.all()

    if 'q' in request.GET:
        q=request.GET['q']
        formm= forum.objects.filter(topic__contains=q)

    else:
        formm = forum.objects.all()
    return render(request,'forum/forum.html', {'formm': formm})  


def forum_singolo(request, slug):
    discussions = Discussione.objects.all().order_by("-id")
    forum_slug= get_object_or_404(forum, slug_title=slug)

    return render(request, 'forum/forum_singolo.html', {'discussions': discussions, 'forum_slug': forum_slug})

def AggiungiForumPreferiti(request):

    if request.method == 'POST':
        form_ = AddPrefe(request.POST)

        if form_.is_valid():
            #qs = form_.save(commit=False)
            #qs.save()
            #form_.save()
            return render(request, 'forum/successo_forum.html')
        else:
            return render(request, 'home/errore.html')
    form_ = AddPrefe()
    context = {
        'form':form_
    }

    return render(request,'forum/addPrefe.html',context)


def addInForum(request):
    form = CretaedInForum()
    if request.method == 'POST':
        form = CretaedInForum(request.POST)

        if form.is_valid():
            form.save()
            return redirect('forum')
    context ={
        'form':form
    }
    return render(request,'forum/addInForum.html',context)

def addInDiscussion(request):
    form = CreateInDiscussion()

     #nel momento in cui aggiungo una nuovo commento nella discussione
    #devo mandare una mail a tutti quelli che seguono il forum
    
    partecipanti = Partecipa_vero.objects.all()

    #for partecipante in partecipanti:
        #inviamo una mail

     #   email = partecipante.user_che_partecipa

      #  tkinter.messages.showinfo(email)

       # send_mail("ciao!", "Qualcuno ha aggiunto qualcosa al forum che stai seguendo!", [email])

    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum')
    context ={'form':form}

    
    return render(request,'forum/addInDiscussion.html',context)