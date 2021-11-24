from django.urls import path
from . import views
from django.conf.urls import url
from orders import views as order_views

urlpatterns = [
    path('orders/<slug:book_slug>/', order_views.cart_add, name='cart_add'),
    path('orders/', order_views.cart_list, name='cart_list'),
]
