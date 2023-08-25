from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('cours/', views.acces_ressource, name='acces_ressource'),
    path('ajax/', views.test_ajax, name = 'test_ajax'),
    path('stats/', views.stats, name='stats'),
    path('test/', views.test, name = 'test'),
    path('google311f29b3ed4bd3be.html', views.google, name='google'),
]
