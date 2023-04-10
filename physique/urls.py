from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('ajax/', views.test_ajax, name = 'test_ajax'),
    path('test/', views.test, name = 'test'),
    path('google311f29b3ed4bd3be.html', views.google, name='google'),
]
