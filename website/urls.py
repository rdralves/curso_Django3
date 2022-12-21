
from django.urls import path
from .views import home
from .views import post_datail

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/', post_datail, name='post_datail')
]
