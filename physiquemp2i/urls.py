from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('physique.urls')),
]
handler404 = 'physique.views.handler404'