from django import forms


class SearchBookForm(forms.Form):
    name = forms.CharField(help_text="Enter a book title or an author", required=False) # noqa
    """
    def clean_name(self):
        data = self.cleaned_data['name']

        if "@" in data or "," in data or "+" in data or "-" in data or "_" in data: # noqaflake8 
            raise ValidationError(_('Invalid name'))

        return data
    """        
