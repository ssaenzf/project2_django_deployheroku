from django.urls import path
from . import views
from django.conf.urls import url
from orders import views as order_views

urlpatterns = [
    path('add/<slug:slug>/', order_views.cart_add, name='cart_add'),
    path('', order_views.cart_list, name='cart_list'),
    path('remove/<slug:slug>/', order_views.cart_remove, name='cart_remove'),
    path('order_create/', order_views.order_create, name='order_create'),
]
