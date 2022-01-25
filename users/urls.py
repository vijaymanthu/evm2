from django.urls import path
from .views import *


urlpatterns = [
    path('', Login, name="login"),
    # path('staffs/', Staffs, name="staffs"),
    path('logout', logout, name='logout'),
]
