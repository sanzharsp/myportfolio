
from django.urls import path
from .views import *

urlpatterns = [

    path('', Main.as_view(),name='main'),
]
