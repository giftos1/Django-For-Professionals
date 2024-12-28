from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template = 'books/book_detail.html'
