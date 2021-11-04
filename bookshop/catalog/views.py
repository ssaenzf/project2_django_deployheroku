from decimal import Context
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Book
from django.db.models import Q

def home(request):
    book_list = Book.objects.all()

    context = {
        'book_list': book_list,
    }

    return render(request, 'home.html', context=context)

def BookDetailView(request):
    model = Book
    queryset = request.GET.get("busqueda")
    libros = Book.objects
    if queryset:
        libros = Book.objects.filter(
            Q(title__icontains = queryset) |
            Q(author__icontains = queryset)
        ).distinct()

    return render(request, 'home.html', {'libros': libros})
    