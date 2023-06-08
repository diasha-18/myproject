from django.http import HttpResponse
from django.shortcuts import redirect
from polls.models import Feedback

def create(request):

    feedback = Feedback()
    feedback.email = request.POST.get("email")
    feedback.text = request.POST.get("message")
    feedback.save()

    return redirect('/')