from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalog.models import Book

@login_required
def cart_remove(request , book_slug):
    book = Book.objects.filter(slug__exact=book_slug)
    cart = Cart(request)
    cart.remove(book)
    return redirect ("cart_list")
