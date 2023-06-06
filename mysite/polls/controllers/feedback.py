from django.shortcuts import redirect
from polls.models import Feedback


def create(request):

    feedback = Feedback()
    feedback.email = request.POST.get("email")
    feedback.text = request.POST.get("message")
    feedback.save()

    return redirect('../index.html/')

def index(request):
    feedbacks = Feedback.object.order_by('created_at')
    content = {'feedbacks': feedbacks}
    return render(request, 'feedback.html', content)
