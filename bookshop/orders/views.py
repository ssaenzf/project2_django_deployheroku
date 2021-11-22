from django.shortcuts import get_object_or_404, render
from . import cart
from orders import forms
from catalog.models import Book

def cart_add(request, book_slug):
    """add the book with slug "book_slug" to the
    shopping cart. The number of copies to be bought
    may be obtained from the form CartAddBookForm """

    cart = Cart(request)
    #cogemos el libro con el slug que se le pasa a la funcion
    book = get_object_or_404(Book, slug=book_slug)

    if request.method == 'POST':
        form = forms.CartAddBookForm(request.POST)
        if form.is_valid():
            #coger units del form
            units = form.cleaned_data['units']
            #Añadirlas al carrito
            cart.add(cart, book, units, True)
            cart.save(cart)
            return render(request, 'cart.html', context={'cart': cart, 'units': units, 'book': book})

class cartView():
    pass