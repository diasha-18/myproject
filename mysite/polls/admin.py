from django.contrib import admin
from .models import Client
from .models import Feedback

admin.site.register(Feedback)
admin.site.register(Client)
