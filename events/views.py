from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from .models import EventInfo
# Create your views here.


def EventRegistration(request):

    return HttpResponse('<h1>Event Registration form</h1>')


def Events(request):
    events = EventInfo.objects.all()
    return render(request, 'events.html')



def home(request):
    return render(request, 'home.html')
