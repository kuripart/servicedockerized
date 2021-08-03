# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from game.views import index

urlpatterns = [
    path('', include('game.urls')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]
