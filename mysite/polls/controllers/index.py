from django.http import HttpResponse
from django.shortcuts import redirect, render
from upload_app.models import Volley
from upload_app.models import Basket
from polls.models import Client
from polls.models import Feedback

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

def show_feedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedback': feedback})