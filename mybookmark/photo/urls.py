from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    path('', views.AlbumLV.as_view(), name='index'),
    path('album', views.AlbumDV.as_view(), name='album_list'),
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
]