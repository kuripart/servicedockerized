## urls.py
from django.urls import path
from game.views import index, game

urlpatterns = [
    ## ... Other URLS
    path('', index),
    path('play/<room_code>', game),
]
