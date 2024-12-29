from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
