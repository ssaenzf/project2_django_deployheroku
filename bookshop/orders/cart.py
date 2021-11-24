from decimal import Decimal
from django.conf import settings
from catalog.models import Book


class Cart(object):


    def __init__(self , request):
        """
        Initialize the cart.
        if request.session[settings.CART_SESSION_ID]
            does not exist create one
        Important: Make a copy of request.session[
            settings.CART_SESSION_ID]
                do not manipulate it directly
                request.session is not a proper
                    dictionary and
                direct manipulation will produce
                    weird results
        """
        # request session is the only variable
        # that persists between two http accesses
        # from the same client

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # If there is no cart create an empty one
            # and save it in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.save()


    def add(self , book , quantity=1, update_quantity=True):
        """
        Add a book to the cart or update quantity if
        book exists. Note , use strings as keys of the
        dictionary since session use JSON module
        to serialize dictionaries and JSON
        many not supports keys that are not strings ,

        For each book store only the ID (as key)
        and a dictionary
        with the price and quantity as value
        {’quantity ’: 0,
         ’price ’: str(book.price)}
        Store ’price’ as a string because a Decimal
            object may not be properlly serialized
        """
        book_id = str(book.id)
        # your code goes here

        # Se obtiene copia de cart ya que al parecer sino falla ya que session
        # no es un diccionario apropiado
        cart = self.session.get(settings.CART_SESSION_ID)
        # Si esta activado actualzar la nueva quantity se sumará a la antigua
        # quantity
        if update_quantity == True:
            # si existe el carro se procede normal ya que si se puede actualizar
            if cart.get(book_id) is not None:
                if cart[book_id]['quantity'] is not None:
                    cart[book_id]['quantity'] = cart[book_id]['quantity'] + int(quantity)
                else:
                    cart[book_id]['quantity'] = int(quantity)

                cart[book_id]['price'] = str(book.price)
            else:
                cart[book_id] = {'quantity': quantity, 'price': str(book.price)}
        else:
            cart[book_id] = {'quantity': quantity, 'price': str(book.price)}

        self.cart = cart
        # end of your code goes here
        self.save()


    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified"
        # to make sure it is saved
        # django saves the session if
        # new pairs key:value are
        # added or deleted but what is
        # modified is inside self.cart
        # and django does not realize
        # that it has been modified.
        self.session.modified = True


    def remove(self , book):
        """
        Remove a book from the cart.
        """
        # your code goes here
        book_id = str(book.id)
        # your code goes here

        # Se obtiene copia de cart ya que al parecer sino falla ya que session
        # no es un diccionario apropiado
        cart = self.session.get(settings.CART_SESSION_ID)

        if cart[book_id]:
            del cart[book_id]
        else:
            printf("Se esta intentando eliminar un libro que no existe")

        # Se guarda la copia de cart modificada en la sesion
        self.cart = cart
        # end of your code goes here
        self.save()
        # endyourcode


    def __iter__(self):
        """
        Iterate over the items (books IDs) in the cart
        and get the books from the database. This function is used by thefor loop.
        for item in self.cart:
            Note: here we add to each item saved in self.
            cart and object
        of type book. This will help us to create
            templates showing
        the book title. We can not add a book object int he method
        "add" becose self.cart is saved at the end of
        the function and a session variable cannot
        be complex , it can only store numbers and
        strings but not object with pointers.
        """
        book_ids = self.cart.keys()
        # get the book objects and add them to the cart
        books = Book.objects.filter(id__in=book_ids)
        for book in books:
            self.cart[str(book.id)]['title'] = book.title

        for item in self.cart.values ():
            # since ’price’ is stored as string cast it to ’decimal ’
            item['price'] = float(item['price'])
            item['total_price'] = float(Decimal(item['price']) * int(item['quantity']))
            yield item


    def __len__(self):
        """
        return the number of items in the cart. That is, the sum of
        the quantities of each book in the cart. If the user
        wants to buy 2 copies of book with id=1 and 4
        copies of book with id=2
        __len__ () should return 6
        """
        # your code goes here
        quantity = 0
        # Se itera sobre los valores y se ira obteniendo el quantity
        for item in self.cart.values ():
            quantity = quantity + item['quantity']

        return quantity
        # endyourcode


    def get_total_price(self):
        """
        returns total amount to be paid for all items
        in the cart
        """
        # your code goes here
        price = 0
        for item in self.cart.values ():
            price = price + (Decimal(item['price']) * int(item['quantity']))

        return price
        # endyourcode


    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
