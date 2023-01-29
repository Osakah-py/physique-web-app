from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('google311f29b3ed4bd3be.html', views.google, name='google'),
]