from django import forms
from .models import home_notizia
from django import forms  



class notizia_form(forms.ModelForm):    
    class Meta:
        model = home_notizia
        fields = ('descrizione', 'nome_notizia')
