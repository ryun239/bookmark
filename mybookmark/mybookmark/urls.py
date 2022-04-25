from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView, DeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
]
