from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.db.models import Q
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
    queryset = Book.objects.all().prefetch_related('reviews__author',)


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_results_list'
    template_name = 'books/search_results.html'

    # queryset = Book.objects.filter(title__icontains='professionals')

    def get_queryset(self):
        query = self.request.GET.get("search")
        # The Q helps us use & | operators for filtering
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
