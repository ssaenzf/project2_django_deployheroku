from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SearchBookForm(forms.Form):
    name = forms.CharField(help_text="Enter a book title or an author", required=False)
    """
    def clean_name(self):
        data = self.cleaned_data['name']

        if "@" in data or "," in data or "+" in data or "-" in data or "_" in data:
            raise ValidationError(_('Invalid name'))

        return data
    """        
