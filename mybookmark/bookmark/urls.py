from django.contrib import admin
from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Bookmark
from .views import BookmarkCreateView, BookmarkChangeLV, BookmarkUpdateView, BookmarkDeleteView

app_name = 'bookmark'
urlpatterns = [
    path('', ListView.as_view(model=Bookmark), name='index'),
    path('<int:pk>', DetailView.as_view(model=Bookmark), name='detail'),

    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('change/', BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name='delete'),
]
