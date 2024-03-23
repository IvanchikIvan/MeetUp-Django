from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path("", views.index),
    path("meet-creation", views.create_meet),
]

