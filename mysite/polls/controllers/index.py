from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import Feedback
from upload_app.models import Volley
from upload_app.models import Basket

def index(request):
    return render(request, 'index.html', {})


def aboutVolley(request):
    items = Volley.objects.all()
    return render(request, 'volleyball.html', {'items': items})


def aboutBasket(request):
    items = Basket.objects.all()
    return render(request, 'basketball.html', {'items': items})


def aboutDelivery(request):
    return render(request, 'delivery.html', {})

def feedback(request):
    return render(request, 'feedback.html', {})