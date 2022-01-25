from django.contrib import admin
from django.db import models
from .models import EventInfo, EventRegistration

# Register your models here.
admin.site.register(EventInfo)
admin.site.register(EventRegistration)
