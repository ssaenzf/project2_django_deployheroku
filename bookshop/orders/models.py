from django.db import models
from catalog.models import Book
from django.utils import timezone
from django.contrib.auth.models import User


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

    def get_total_cost(self):
        order_items = OrderItem.objects.filter(order=self)
        cost = 0
        for item in order_items:
            cost = cost + item.get_total_cost()
        return cost

    def save(self, *args, **kwargs):
        ''' On save or update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()

        return super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    quantity = models.IntegerField(null=False, default=0)

    def get_total_cost(self):
        return self.price * self.quantity

    # Cada vez que guarda order item, se guardan estos order items en una lista de items
    # para su order correspondiente con el fin de satisfacer el test
    def save(self, *args, **kwargs):
        return super(OrderItem, self).save(*args, **kwargs)
