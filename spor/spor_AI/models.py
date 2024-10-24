from django.db import models

# Create your models here.

class Sporcu(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    dogum_tarihi = models.DateField()  # dogum_tarihi doğru yazıldı
    kilo = models.DecimalField(max_digits=5, decimal_places=2)
    boyUzunlugu = models.DecimalField(max_digits=5, decimal_places=2)
    kacAylik = models.IntegerField()
    ekstra_aciklama = models.TextField(blank=True, null=True)  # Yeni alan eklendi

    class Meta:
        verbose_name_plural = 'Sporcular'
        verbose_name = 'Sporcu'

    def __str__(self):
        return f"{self.ad} {self.soyad}"
