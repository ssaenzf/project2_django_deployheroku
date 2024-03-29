from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('searching/', views.search, name='search'),
    path('search/book/<slug:slug>/', views.book_detail_view, name='detail'),
    path('search/<str:q>', views.BookListView.as_view(), name='searchedbook'),
    path('search/', views.BookListView.as_view(), name='searchedbook'),
]
