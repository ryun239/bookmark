import imp
from re import I
from django.contrib import admin
from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Bookmark

#app_name = 'bookmark'
urlpatterns = [
    path('', ListView.as_view(model=Bookmark), name='index'),
    path('<int:pk>', DetailView.as_view(model=Bookmark), name='detail'),
]
