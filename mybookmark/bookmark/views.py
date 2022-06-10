from operator import mod
from django import views
from .models import Bookmark
from django.views.generic import ListView, DeleteView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mybookmark.views import OwnerOnlyMixin 

class BookamekLV(ListView):
    model = Bookmark

class bookmarkDV(DeleteView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model  = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
    
class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']

    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
    