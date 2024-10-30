from django.contrib import admin
from .models import Sporcu

class SporcuAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad', 'soyad', 'dogum_tarihi', 'kilo', 'boyUzunlugu', 'kacAylik')  # 'boy' yerine 'boyUzunlugu' kullanıldı

admin.site.register(Sporcu, SporcuAdmin)
