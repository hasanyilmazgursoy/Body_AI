from django.shortcuts import render

# Create your views here.

def anasayfa(request):
    return render(request, 'index.html')

def hakkimizda(request):
    return render(request, 'hakkimizda.html')