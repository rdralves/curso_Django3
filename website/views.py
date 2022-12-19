from django.shortcuts import render
from modus import app
from .models import Post


# Create your views here.


# def blog(request):
    
#     return render(request, 'index.html')


def lis(request):
    lista = app.lista
    posts = Post.objects.all()
    data = {
        'post': posts,
        'lis': lista
    }
    return render(request, 'index.html', data)
