from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

import physiquemp2i.admin

from django.conf.urls import handler404
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chimie/', include('chimie.urls')),
    path('', include('physique.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'physique.views.handler404'

if settings.DEBUG:
    urlpatterns += [
        # Serve les fichiers de média en utilisant Django pendant le développement
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]