from django.contrib import admin
from django.urls import path
from .views import contact, about, home

urlpatterns = [
    path('', home),
    path('me', about),
    path('contact', contact),
]
