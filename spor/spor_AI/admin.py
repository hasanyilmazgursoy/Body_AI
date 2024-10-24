from django.contrib import admin
from .models import Sporcu  # Model adı büyük harfle güncellendi

class SporcuAdmin(admin.ModelAdmin):
    list_display = ['ad', 'soyad', 'dogum_tarihi', 'kilo', 'boyUzunlugu', 'kacAylik', 'ekstra_aciklama']  # ekstra_aciklama eklendi
    search_fields = ['ad', 'soyad']

admin.site.register(Sporcu, SporcuAdmin)

#gün
