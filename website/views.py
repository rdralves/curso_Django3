from django.shortcuts import render
from modus import app
from .models import Post

# Create your views here.


def blog(request):
    
    lista = [
        'Django 3', 'Python', 'Git'
    ]

    list_posts = Post.objects.all()
    ola = app.ola()
    data = {
        'ola': ola,
        'name': 'Curso de Django 3',
        'lista_tecnologias': lista,
        'posts': list_posts
    }

    return render(request, 'index.html', data)
