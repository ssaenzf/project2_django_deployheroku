from .cart import Cart

# added
def cart(request):
    return {'cart': Cart(request)}
