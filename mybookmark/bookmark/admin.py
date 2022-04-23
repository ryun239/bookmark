from django.contrib import admin
from .models import Bookmark

# Register your models here.
#@admin.register
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')


admin.site.register(Bookmark, BookmarkAdmin)
