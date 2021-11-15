from django.db import models
from bookshop.catalog.models import Book


class Order(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()
    paid = models.BooleanField(default = False)


    def save(self, *args, **kwargs):
        ''' On save or update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()

        return super(User, self).save(*args, **kwargs)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    quantity = models.IntegerField(null=False, default=0)
