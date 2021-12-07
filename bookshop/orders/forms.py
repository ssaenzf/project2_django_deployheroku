from django import forms

class CartAddBookForm(forms.Form):
    units = forms.IntegerField()

class OrderCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
