from django import forms

class CartAddBookForm(forms.Form):
    units = forms.IntegerField()