from django.shortcuts import render
from .models import Bookmark
from django.views.generic import ListView, DeleteView

# Create your views here.

class BookamekLV(ListView):
    print('in List?')
    model = Bookmark

class bookmarkDV(DeleteView):
    print('in Detail?')
    model = Bookmark
