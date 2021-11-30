from .cart import Cart


def cart(request):
    return {'cart': Cart(request), 'size': int(Cart(request).__len__())}
