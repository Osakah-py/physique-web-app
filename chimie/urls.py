from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('capture-the-flag', views.inte, name='inte')
]
