from django.shortcuts import render, redirect
from .forms import SporcuForm
from .models import Sporcu
import os


def anasayfa(request):
    chatbox_visible = False
    if request.method == 'POST':
        form = SporcuForm(request.POST)
        if form.is_valid():
            # Form geçerli ise, veriyi kaydet
            sporcu = form.save()  # Sporcu modeline göre kaydediyoruz

            # Kullanıcı bilgilerini bir TXT dosyasına yazma
            with open('sporcu_bilgileri.txt', 'a') as file:  # Dosyayı ekleme modunda açıyoruz
                file.write(f"Ad: {sporcu.ad}, Soyad: {sporcu.soyad}, Doğum Tarihi: {sporcu.dogum_tarihi}, "
                           f"Kilo: {sporcu.kilo}, Boy Uzunluğu: {sporcu.boyUzunlugu}, "
                           f"Kaç Aylık: {sporcu.kacAylik}, Ekstra Açıklama: {sporcu.ekstra_aciklama}\n")

            chatbox_visible = True
            # Formu temizlemek isterseniz:
            form = SporcuForm()  # Formu sıfırlayarak yeni bir giriş yapılmasını sağlayabilirsiniz
    else:
        form = SporcuForm()  # İlk yüklemede boş form

    context = {
        'form': form,
        'chatbox_visible': chatbox_visible,
    }
    return render(request, 'index.html', context)


def hakkimizda(request):
    return render(request, 'hakkimizda.html')
