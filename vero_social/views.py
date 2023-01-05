from contextlib import _RedirectStream
import tkinter
from urllib import request

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from vero_social.forms import PostForm

from .models import Like_vero, Post_vero, tag_piaciuti

# Create your views here.

def social(request):

    qs = Post_vero.objects.all().order_by("-id")
    post_raccomandation = Post_vero.objects.all().order_by("id")

    tags = tag_piaciuti.objects.all()

    user = request.user

    context={
        'qs': qs,
        'tags': tags,
        'user': user,
        'post_raccomandation': post_raccomandation,
    }

    return render(request,'vero_social/social.html', context)

def like_post(request):
    user = request.user
    
    #se schiaccio il pulsante like
    if request.method == 'POST':

        post_id = request.POST.get('post_id')
        post_obj = Post_vero.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            coppia_tag_nome = tag_piaciuti(username=request.user.get_username(), tag=post_obj)
            coppia_tag_nome.save()
            post_obj.liked.add(user)

        like, created = Like_vero.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == "Like":

                like.value = "Unlike"
            else:
                like.value = "Like"
        like.save()
    return redirect('social')


def who_likes(request, slug):
    lik = Like_vero.objects.all()
    post_slug= get_object_or_404(Post_vero, slug_title=slug)

    return render(request,'vero_social/who_likes.html', {'lik': lik, 'post_slug': post_slug})

    
def inserisci_nuovo_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user)
            post.save()
            messages.success(request, 'Post pubblicato con successo')
            return redirect('social')
        else:
            messages.success(request, 'Qualcosa è andato storto, riprovare')

    form = PostForm()  
    context = {  
        'form':form  
    }  
    
    return render(request, 'vero_social/nuovo_post.html', context)

