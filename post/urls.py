from django.urls import path
from .views import *

urlpatterns = [
    path('this_time/', this_time),
    path('aboat_us/', aboat_us),
    path('', home)
]
