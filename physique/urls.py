from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('cours/', views.acces_ressource, name='acces_ressource'),
    path('stats/', views.stats, name='stats'),
    path('test/', views.test, name = 'test'),
    path('google311f29b3ed4bd3be.html', views.google, name='google'),
    # urls ajax
    path('ajax/more', views.more_ajax, name = 'ajax more'),
    path('ajax/add', views.add_ajax, name = 'ajax add'),
]
