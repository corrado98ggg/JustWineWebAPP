from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

from .forms import ContactForm

def contattaci(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            nome= form.cleaned_data['nome']
            email = form.cleaned_data['email']
            contenuto = form.cleaned_data['contenuto']

            html = render_to_string('contattaci/contatti.html', {
                'nome': nome,
                'email': email,
                'contenuto': contenuto
            })

            send_mail(nome, contenuto, email, ['provasitounimore@gmail.com'], html_message=html)

            return render(request, 'contattaci/successo_contatti.html')
        
        else:
            return render(request, 'home/errore.html')
    else:
            form = ContactForm()

    return render(request, 'contattaci\contatti.html', {
        'form': form
    })
