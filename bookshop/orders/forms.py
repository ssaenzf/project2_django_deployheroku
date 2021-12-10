from django import forms

CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
    ("6", "Six"),
    ("7", "Seven"),
    ("8", "Eight"),
    ("9", "Nine"),
    ("10", "Ten"),
    ("11", "Eleven"),
    ("12", "Twelve"),
    ("13", "Thirteen"),
    ("14", "Fourteen"),
    ("15", "Fiveteen"),
    ("16", "Sixteen"),
    ("17", "Seventeen"),
    ("18", "Eighteen"),
    ("19", "Nineteen"),
    ("20", "Twenty"),
)

class CartAddBookForm(forms.Form):
    quantity = forms.ChoiceField(choices = CHOICES, help_text='This field is required.')

class OrderCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    address = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
