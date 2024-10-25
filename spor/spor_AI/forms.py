# forms.py
from django import forms
from .models import Sporcu

class SporcuForm(forms.ModelForm):
    class Meta:
        model = Sporcu
        fields = ['ad', 'soyad', 'dogum_tarihi', 'kilo', 'boyUzunlugu', 'kacAylik', 'ekstra_aciklama']
