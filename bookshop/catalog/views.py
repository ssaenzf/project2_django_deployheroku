from decimal import Context
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Book
from django.db.models import Q
from .forms import SearchBookForm

def home(request):
    book_list = Book.objects.all()

    context = {
        'book_list': book_list,
    }

    return render(request, 'home.html', context=context)

def search(request):
    return render(request, 'search.html')

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("busqueda")
        print(self.model)
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'    