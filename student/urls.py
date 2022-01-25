from django.urls import path
from .views import *


urlpatterns = [

    path('', Students.get, name="student"),
    path('view_status', Students.viewStatus, name="view_status"),
    path('profile', Students.profile, name="profile"),
    path('event_reg/', Students.eventRegistrations, name="event_reg"),
    path('dr/<int:id>',Students.deleteRegistration,name="delete_reg")
]

