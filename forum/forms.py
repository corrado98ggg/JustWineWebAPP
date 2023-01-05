from django.forms import ModelForm
from .models import *
from django.contrib.auth import get_user_model

class AddPrefe(ModelForm):
    class Meta:
        model = Partecipa_vero
        fields = '__all__'

class CretaedInForum(ModelForm):
    class Meta:
        model = forum
        fields = ('nome', 'email', 'topic', 'descrizione')

class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussione
        fields = ('nome_forum_associato', 'forum', 'discuss', 'username')

