from django.shortcuts import render
from django.views import generic
from .models import Book, Comment, Author
from django.shortcuts import get_object_or_404


def home(request):
    book_list = Book.objects.all()
    book_score = Book.objects.order_by('-score')[0:5]
    book_date = Book.objects.order_by('-date')[0:5]
    context = {
        'book_list': book_list,
        'book_score': book_score,
        'book_date': book_date
    }

    return render(request, 'home.html', context=context)


def search(request):
    return render(request, 'search.html')


class ListAsQuerySet(list):

    def __init__(self, *args, model, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        book_list = Book.objects.all()
        if query:
            object_list = list(Book.objects.filter(title__icontains=query))
            object_list.extend(list(Book.objects.filter(author__in=Author.objects.filter(first_name__icontains=query)))) # noqa
            object_list.extend(list(Book.objects.filter(author__in=Author.objects.filter(last_name__icontains=query)))) # noqa
            object_list = set(object_list)
            book_list = list(object_list)
            book_list = ListAsQuerySet(book_list, model=Book)

        return book_list


def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    comments = Comment.objects.filter(book=book)
    return render(request, 'book_detail.html', context={'book': book, 'comments': comments}) # noqa
