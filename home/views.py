from django.shortcuts import render
from django.http import HttpResponse


sig = 'SIG SANLIS | '

def home(request):
    title = sig + 'Home'
    return render(request, 'index.html', {'title': title})


def about(request):
    title = sig + 'Sobre'
    return render(request, 'about.html', {'title': title})


def contact(request):
    title = sig + 'Contato'
    return render(request, 'contact.html', {'title': title})
