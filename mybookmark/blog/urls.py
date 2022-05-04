import imp
from re import I
from django import views
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from blog import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.PostLV.as_view(), name='index'),
    # /blog/post/
    path('post/', views.PostLV.as_view(), name='post_list'),
    # /blog/post/djagno-example
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    # /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    # /blog/archive/2019/
    path('archive/<int:year>',views.PostYAV.as_view(), name='post_year_archive'),
    # /blog/arvhive/2019/nov/
    path('archive/<int:year>/<str:month>',views.PostMAV.as_view(), name='post_month_archive'),
    # /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:dat>',views.PostDAV.as_view(), name='post_day_archive'),
    # /blog/archive/today/
    path('archive/<today>',views.PostTAV.as_view(), name='post_today_archive'),
    # /blog/tag/
    path('tag/',views.TagCloudTV.as_view(), name='tag_cloud'),
    # /blog/tag/tagname/
    path('tag/<str:tag>',views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    # /blog/search
    path('search/', views.SearchFromViews.as_view(), name='search'),
]