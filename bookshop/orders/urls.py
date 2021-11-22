from django.urls import path
from . import views
from django.conf.urls import url
from orders import views as order_views

urlpatterns = [
    path('cart/', order_views.cart_add, name='cart_list'),
]
