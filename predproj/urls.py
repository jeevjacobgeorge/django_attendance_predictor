
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import algorithm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('algorithm.al_urls')),
    path('attendance',include('algorithm.al_urls')),
]

