from django import forms


class SearchBookForm(forms.Form):
    """
    Esta clase define el formulario
    usado para la búsqueda de libros
    AUTOR: Carolina Monedero
    """

    name = forms.CharField(help_text="Enter a book title or an author", required=False) # noqa