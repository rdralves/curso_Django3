from django.shortcuts import render
from modus import app
from .models import Post


# Create your views here.


# def blog(request):
    
#     return render(request, 'index.html')


def home(request):
    lista = app.lista
    posts = Post.objects.all()
    data = {
        'post': posts,
        'lis': lista
    }
    return render(request, 'index.html', data)


def post_datail(request, id):
    post= Post.objects.get(id=id)
    return render(request, 'post_datail.html', {'post': post})