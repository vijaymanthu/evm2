from django.urls import path
from .views import *



urlpatterns = [
    
    path('', Staff.get, name="staffs"),
    path('registered_std',getRegisteredstudents,name="getregisteredStd")
]