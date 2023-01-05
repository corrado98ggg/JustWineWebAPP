from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=255)
    email = forms.EmailField()
    contenuto = forms.CharField(widget=forms.Textarea)