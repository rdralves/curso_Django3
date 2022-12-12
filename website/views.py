from django.shortcuts import render
from modus import app

# Create your views here.


def blog(request):
    
    lista = [
        'Django 3', 'Python', 'Git'
    ]

    ola = app.ola()
    data = {
        'ola': ola,
        'name': 'Curso de Django 3',
        'lista_tecnologias': lista
    }

    return render(request, 'index.html', data)
