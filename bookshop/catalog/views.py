from django.shortcuts import render
from django.views import generic
from .models import Book, Comment, Author
from django.shortcuts import get_object_or_404
from orders.forms import CartAddBookForm


def home(request):
    """
    Esta función implementa la vista de la pagina
    home.html pasandole las variables book_list,
    book_score y book_date como contexto a la plantilla
    AUTOR: Santos Saenz
    """
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
    """
    Esta función implementa la vista de la pagina
    search.html
    AUTOR: Carolina Monedero
    """
    return render(request, 'search.html')


class ListAsQuerySet(list):
    def __init__(self, *args, model, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)


class BookListView(generic.ListView):
    """
    Esta clase implementa la vista de la pagina
    book_list.html donde se muestra una lista de los libros
    que coinciden conla búsqueda realizada
    AUTOR: Carolina Moneder
    """
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5

    def get_queryset(self):
        """
        Esta función devuelve el conjunto de libros
        que coinciden con la búsqueda realizada
        AUTOR: Carolina Monedero
        """
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
    """
    Esta clase implementa la vista de la pagina
    book_detail.html donde se muestra la página de
    detalles de un libro determinado
    AUTOR: Carolina Monedero
    """
    book = get_object_or_404(Book, slug=slug)
    comments = Comment.objects.filter(book=book)
    form = CartAddBookForm()
    return render(request, 'book_detail.html', context={'book': book, 'comments': comments, 'form': form}) # noqa
