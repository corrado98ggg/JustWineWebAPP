"""sito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from vero_social.views import inserisci_nuovo_post, who_likes
from home.views import inserisci_nuova_notizia
from forum.views import addInDiscussion, addInForum, forum_singolo, AggiungiForumPreferiti

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('malattie/', include('malattie.urls')),
    path('contatti/', include('contattaci.urls')),
    path('signup/', include('registration.urls')),
    path('login/', include('registration.urls_login')),
    path('logout/', include('registration.urls_logout')),
    path('social/', include('vero_social.urls')),
    path('change_password/', include('registration.urls_change')),
    path('forum/', include('forum.urls')),
    
    path('nuovo_post/', inserisci_nuovo_post, name="inserisci_nuovo_post"),

    path('nuova_notizia/', inserisci_nuova_notizia, name="inserisci_nuova_notizia"),

    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
    path('AggiungiForumPreferiti/', AggiungiForumPreferiti, name='AggiungiForumPreferiti'),   

    path('forum_singolo/<slug:slug>/',forum_singolo,name='forum_singolo'),

    path('like/<slug:slug>/',who_likes,name='who_likes'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
