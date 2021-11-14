from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    Esta clase define el formulario
    usado para crear una cuenta nueva
    AUTOR: Santos Saenz
    """
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.') # noqa

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
