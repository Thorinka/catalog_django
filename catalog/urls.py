from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
