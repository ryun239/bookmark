from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView, DeleteView
from .views import HomeView
from .views import UserCreateView, UserCreateDoneTV

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/', UserCreateView.as_view(), name='register'),
    path('account/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
