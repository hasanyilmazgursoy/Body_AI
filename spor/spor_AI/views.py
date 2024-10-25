# views.py
from django.shortcuts import render, redirect
from .models import Sporcu
from .forms import SporcuForm


def anasayfa(request):
    form = SporcuForm()
    chatbox_visible = False

    if request.method == 'POST':
        form = SporcuForm(request.POST)
        if form.is_valid():
            form.save()
            chatbox_visible = True  # Chatbox görünür

    context = {
        'form': form,
        'chatbox_visible': chatbox_visible
    }
    return render(request, 'index.html', context)


def hakkimizda(request):
    return render(request, 'hakkimizda.html')  # 'hakkimizda.html' yerine ilgili şablon dosyanızın adını yazın