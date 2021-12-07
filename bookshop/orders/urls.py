from django.urls import path
from . import views
from django.conf.urls import url
from orders import views as order_views

urlpatterns = [
    path('orders/add/<slug:book_slug>/', order_views.cart_add, name='cart_add'),
    path('orders/', order_views.cart_list, name='cart_list'),
    path('orders/remove/<slug:book_slug>/', order_views.cart_remove, name='cart_remove'),
    path('orders/order_create/', order_views.order_create, name='order_create'),
]
