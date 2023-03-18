from django.urls import path, include

from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('magazin/',all, name='qarz'),
    path('qarz/<int:test_id>', index ,name="quiz"),
    path('xarajat/',xarajat, name='xar'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)