
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("robot.txt", views.robot),
    path("sitemap", views.sitemap)
]
