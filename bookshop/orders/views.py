from django.shortcuts import get_object_or_404, render
from . import cart
from django.contrib.auth.decorators import login_required
from orders import forms
from catalog.models import Book

def cart_add(request, book_slug):
    """add the book with slug "book_slug" to the
    shopping cart. The number of copies to be bought
    may be obtained from the form CartAddBookForm """

    carro = cart.Cart(request)
    #cogemos el libro con el slug que se le pasa a la funcion
    book = get_object_or_404(Book, slug=book_slug)

    query = request.POST.get('quantity')
    if query:
        carro.add(book, query, True)
        items = carro.__iter__()
        total_price = carro.get_total_price()
        return render(request, 'cart.html', context={'items':items, 'total_price':total_price})

    else:
        return redirect(book.get_absolute_url)


class cartView():
    pass

@login_required
def cart_remove(request , book_slug):
    book = Book.objects.filter(slug__exact=book_slug)
    cart = Cart(request)
    cart.remove(book)
    return redirect ("cart_list")   # Esto hay que ver
