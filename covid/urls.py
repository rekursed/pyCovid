from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from covid import views
app_name = 'covid'

urlpatterns = [
    path('all', views.getAll),
]