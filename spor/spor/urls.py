from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from spor_AI.views import anasayfa, hakkimizda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', anasayfa, name='anasayfa'),  # İsimlendirme eklendi
    path('hakkimizda/', hakkimizda, name='hakkimizda'),  # İsimlendirme eklendi
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
