from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html')


def aboutVolley(request):
    return render(request, 'volleyball.html')


def aboutBasket(request):
    return render(request, 'basketball.html')


def aboutFoot(request):
    return render(request, 'football.html')


def aboutDelivery(request):
    return render(request, 'delivery.html')
