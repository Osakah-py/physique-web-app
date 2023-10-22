from django.urls import path
from . import views

urlpatterns = [
    path('ajax/more', views.more_ajax, name = 'ajax more'),
    path('ajax/add', views.add_ajax, name = 'ajax add'),
]