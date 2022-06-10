import imp
from re import I
from django import views
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from .views import *

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', PostLV.as_view(), name='index'),
    # /blog/post/
    path('post/', PostLV.as_view(), name='post_list'),
    # /blog/post/djagno-example
    re_path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    # /blog/archive/
    path('archive/', PostAV.as_view(), name='post_archive'),
    # /blog/archive/2019/
    path('archive/<int:year>', PostYAV.as_view(), name='post_year_archive'),
    # /blog/arvhive/2019/nov/
    path('archive/<int:year>/<str:month>', PostMAV.as_view(), name='post_month_archive'),
    # /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:dat>', PostDAV.as_view(), name='post_day_archive'),
    # /blog/archive/today/
    path('archive/<today>', PostTAV.as_view(), name='post_today_archive'),
    # /blog/tag/
    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),
    # /blog/tag/tagname/
    path('tag/<str:tag>', TaggedObjectLV.as_view(), name='tagged_object_list'),
    # /blog/search
    path('search/', SearchFromViews.as_view(), name='search'),

    path('add/', PostCreateView.as_view(), name='add'),
    path('change/', PostChangeView.as_view(), name='change'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete'),
]