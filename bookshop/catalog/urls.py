from django.urls import path, reverse
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('search/', views.search, name='search'),
  #  path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('search/<slug:slug>/', views.book_detail_view, name='detail'),
]
