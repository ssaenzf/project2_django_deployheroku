from django.shortcuts import get_object_or_404, render, redirect
# from . import cart
from .cart import Cart
from django.contrib.auth.decorators import login_required
from orders.forms import CartAddBookForm, OrderCreateForm
from catalog.models import Book
# from django.conf import settings
from .models import Order, OrderItem


@login_required
def cart_add(request, slug):
    """
    Esta función añade el libro con slug
    "slug" al carrito.
    AUTOR: Carolina Monedero
    """
    carro = Cart(request)
    # cogemos el libro con el slug que se le pasa a la funcion
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = CartAddBookForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            carro.add(book, quantity, True)
            carro.save()
            return redirect('cart_list')
    else:
        return redirect(book.get_absolute_url)


@login_required
def cart_list(request):
    """
    Esta función implementa la vista de la pagina
    cart.html pasandole las variables items,
    y total_price como contexto a la plantilla
    AUTOR: Carolina Monedero
    """
    carro = Cart(request)
    items = carro.__iter__()
    total_price = carro.get_total_price()
    return render(request, 'cart.html', context={'items': items, 'total_price': total_price})  # noqa


@login_required
def cart_remove(request, slug):
    """
    Esta función elimina un libro con slug
    "slug" del carrito.
    AUTOR: Santos Saenz
    """
    book = Book.objects.filter(slug__exact=slug)[0]
    cart = Cart(request)
    cart.remove(book)
    cart.save()
    return redirect("cart_list")   # Esto hay que ver


def order_create(request):
    """
    Esta función implementa la vista de la pagina
    create.html pasandole la variable form
    como contexto a la plantilla.
    AUTOR: Santos Saenz
    """
    # If this is a POST request then process the Form data
    if request.method == 'POST':
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
                order_item.book = Book.objects.filter(slug__exact=item['slug'])[0]  # noqa
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
    return render(request, 'create.html', context=context)
