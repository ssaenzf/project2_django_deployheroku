from django import forms
from orders.models import Order
from django.forms import ModelForm
CHOICES = (
    ((1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, 7),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "11"),
        (12, "12"),
        (13, "13"),
        (14, "14"),
        (15, "15"),
        (16, "16"),
        (17, "17"),
        (18, "18"),
        (19, "19"),
        (20, "20"),)
)


class CartAddBookForm(forms.Form):
    """
    Esta clase define el formulario
    usado para añadir un libro
    al carrito
    AUTOR: Santos Saenz
    """

    quantity = forms.IntegerField()


"""
class OrderCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    address = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)

    def save(self):
        order = Order(first_name=first_name, last_name=self.last_name,
                      email=self.email, address=self.address,
                      postal_code=self.postal_code, city=self.city)
        order.save()
"""


class OrderCreateForm(ModelForm):
    """
    Esta clase define el formulario
    usado para crear un pedido
    AUTOR: Santos Saenz
    """
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']  # noqa
