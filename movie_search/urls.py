from django.contrib import admin
from django.urls import path, include
from movie_api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urls))
]
