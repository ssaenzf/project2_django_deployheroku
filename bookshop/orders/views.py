from django.shortcuts import get_object_or_404, render, redirect
#from . import cart
from .cart import Cart
from django.contrib.auth.decorators import login_required
from orders.forms import OrderCreateForm
from catalog.models import Book
from django.conf import settings
from .models import Order, OrderItem

def cart_add(request, book_slug):
    """add the book with slug "book_slug" to the
    shopping cart. The number of copies to be bought
    may be obtained from the form CartAddBookForm """

    #carro = cart.Cart(request)
    carro = Cart(request)
    #cogemos el libro con el slug que se le pasa a la funcion
    book = get_object_or_404(Book, slug=book_slug)
    if request.method == 'post':

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            print(quantity)
            carro.add(book, quantity, True)
            carro.save()
            return redirect ('cart_list')
    else:
        return redirect(book.get_absolute_url)


def cart_list(request):
    #carro = cart.Cart(request)
    carro = Cart(request)
    items = carro.__iter__()
    total_price = carro.get_total_price()
    return render(request, 'cart.html', context={'items':items, 'total_price':total_price})


def cart_remove(request , book_slug):
    print("123")
    book = Book.objects.filter(slug__exact=book_slug)[0]
    print(book)
    cart = Cart(request)
    cart.remove(book)
    cart.save()
    return redirect ("cart_list")   # Esto hay que ver

def order_create(request):
    print("bien")
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        print("mal")
        form = OrderCreateForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # Se obtiene y guarda el objeto order
            order = Order()
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.email = form.cleaned_data['email']
            order.address = form.cleaned_data['address']
            order.postal_code = form.cleaned_data['postal_code']
            order.city = form.cleaned_data['city']
            order.paid = True
            order.save()
            # Se obtienen los order items del carro y se guardan
            carro = Cart(request)
            items = carro.__iter__()
            for item in items:
                order_item = OrderItem()
                order_item.order = order
                order_item.price = item['price']
                order_item.quantity = item['quantity']
                order_item.book = Book.objects.filter(slug__exact=item['slug'])[0]
                order_item.save()
            # redirect to a new URL:
            carro.clear()
            context = {
                'order_number': order.id,
            }
            return render(request, 'created.html', context)

    # If this is a GET (or any other method) create the default form.
    else:
        form = OrderCreateForm()
    context = {
        'form': form,
    }
    print("bien3")
    return render(request, 'create.html', context=context)
