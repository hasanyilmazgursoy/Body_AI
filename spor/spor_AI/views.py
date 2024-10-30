from django.shortcuts import render, redirect
from .forms import SporcuForm
from .models import Sporcu

def anasayfa(request):
    chatbox_visible = False
    form = SporcuForm()  # İlk yüklemede boş form

    if request.method == 'POST':
        form = SporcuForm(request.POST)
        if form.is_valid():
            sporcu = form.save()  # Sporcu modeline göre kaydediyoruz
            chatbox_visible = True  # Chatbox'ı görünür yap
            form = SporcuForm()  # Formu sıfırlamak için yeni bir form oluştur

    context = {
        'form': form,
        'chatbox_visible': chatbox_visible,
    }
    return render(request, 'index.html', context)

def hakkimizda(request):
    return render(request, 'hakkimizda.html')
