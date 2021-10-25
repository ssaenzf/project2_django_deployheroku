from django.db import models
from django.urls import reverse
# Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Book(models.Model):
    """Model representing a book """
    title = models.CharField(max_length=100)
    helptext2 = '13 Character <a href="https://www.isbn-international.org'
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text=helptext2)
    price = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    path_to_cover_image = models.CharField(max_length=200)
    number_copies_stock = models.IntegerField(null=False)
    date = models.DateTimeField(null=True)
    score = models.IntegerField(null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ManyToManyField(Author)

    def save(self, *args, **kwargs):
        if self.score < 0:
            self.score = 0
        if self.score > 10:
            self.score = 10
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


class Comment(models.Model):

    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    msg = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.book.__str__() + self.user.__str__() + self.msg
