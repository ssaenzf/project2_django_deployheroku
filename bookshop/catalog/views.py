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

    context = {
        'book_list': book_list,
    }

    return render(request, 'home.html', context=context)

def search(request):
    if request.GET.get("word") != "":
        return redirect(reverse('catalog:searchedbook'))
    else:
        print(request.GET.get("word"))
        return render(request, 'search.html')

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5
    def get_queryset(self):
        query = request.GET.get("word")
        if query:
            object_list = Book.objects.filter(title__icontains=query)
            object_list.extend(Book.objects.filter(author__in=Author.model.objects.filter(first_name__icontains=query)))
            object_list.extend(Book.objects.filter(author__in=Author.model.objects.filter(last_name__icontains=query)))
        else:
            object_list = self.model.objects.all()
        return object_list

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
