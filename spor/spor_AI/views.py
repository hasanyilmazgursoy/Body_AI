from django.shortcuts import render
from .models import Sporcu

# Create your views here.

def anasayfa(request):
    sporcu= Sporcu.objects.all()
    return render(request, 'index.html',{'sporcu':sporcu})

def hakkimizda(request):
    return render(request, 'hakkimizda.html')