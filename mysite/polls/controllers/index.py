from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html', {})
def about(request):
    return render(request, 'about.html')
def aboutRun(request):
    return HttpResponse("RUN")
def aboutVolley(request):
    return HttpResponse("Volleyball")
def aboutBasket(request):
    return HttpResponse("Basketball")
def aboutFoot(request):
    return HttpResponse("Football")
def aboutDelivery(request):
    return HttpResponse("Delivery")
