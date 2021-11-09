from decimal import Context
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import Book, Comment, Author
from django.db.models import Q
from .forms import SearchBookForm
from django.shortcuts import get_object_or_404

def home(request):
    book_list = Book.objects.all()
    book_score = Book.objects.order_by('-score')[0:5]
    book_date = Book.objects.order_by('-date')[0:5]
    context = {
        'book_score': book_score,
        'book_date': book_date
    }

    return render(request, 'home.html', context=context)

def search(request):
    return render(request, 'search.html')
    """return (redirect(reverse('searchedbook', kwargs={'q': request.GET.get('q')})))"""


class ListAsQuerySet(list):

    def __init__(self, *args, model, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)
    """
    def filter(self, *args, **kwargs):
        return self  # filter ignoring, but you can impl custom filter

    def order_by(self, *args, **kwargs):
        return self
    """

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = list(Book.objects.filter(title__icontains=query))
            object_list.extend(list(Book.objects.filter(author__in=Author.objects.filter(first_name__icontains=query))))
            object_list.extend(list(Book.objects.filter(author__in=Author.objects.filter(last_name__icontains=query))))
            object_list = set(object_list)
            book_list = list(object_list)
            book_list = ListAsQuerySet(book_list, model=Book)

        return book_list

def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    comments = Comment.objects.filter(book=book)
    return render(request, 'book_detail.html', context={'book': book, 'comments':comments})
"""
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
"""
