from django.urls import path, reverse
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('books/<search>', views.BookListView.as_view()),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
