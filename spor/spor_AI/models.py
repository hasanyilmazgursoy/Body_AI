from django.db import models

class Sporcu(models.Model):
    ad = models.CharField(max_length=100, verbose_name='Ad')
    soyad = models.CharField(max_length=100, verbose_name='Soyad')
    dogum_tarihi = models.DateField(verbose_name='Doğum Tarihi')  # Doğum tarihi doğru yazıldı
    kilo = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Vücut Ağırlığı')
    boyUzunlugu = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Boy Uzunluğu')
    kacAylik = models.IntegerField(verbose_name='Kaç aylık yazılmak istiyorsunuz ?')
    ekstra_aciklama = models.TextField(blank=True, null=True, verbose_name='Eklemek istedikleriniz')  # Yeni alan eklendi

    class Meta:
        verbose_name_plural = 'Sporcular'
        verbose_name = 'Sporcu'

    def __str__(self):
        return f"{self.ad} {self.soyad}"
