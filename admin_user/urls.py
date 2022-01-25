from django.urls import path
from .views import *


urlpatterns = [

    path('events/', Events.get, name="events"),
    path('addEvent/', Events.add, name="add_event"),
    path('events/d/<int:id>', Events.delete, name="delete_event"),
    path('events/<int:id>', Events.update, name="update_event"),
    path('', Admin, name="admin"),
]
