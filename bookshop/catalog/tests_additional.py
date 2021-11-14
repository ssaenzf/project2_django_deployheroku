import sys
from django.test import TestCase

from catalog.models import Book, Comment, Author
from faker import Faker
from django.test import Client
from django.urls import reverse


class AdditionalTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        try:
            from catalog.management.commands.populate import Command
            populate = Command()
            populate.handle()
        except ImportError:
            print('The module populate_catalog does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except Exception:
            print('Something went wrong in the populate() function :-(')
            raise

    """ Test para comprobar que si introducimos libros con score incorrectos estos
    se actualizan a scores correctos """
    def test_book_score(self):
        faker = Faker()
        # Score negativo
        book1 = Book()
        book1.id = 1
        book1.title = faker.name()
        book1.isbn = "1234" + str(book1.id)
        book1.price = faker.random_int(min=1, max=100)
        book1.number_copies_stock = faker.random_int(min=1, max=20)
        book1.date = faker.past_datetime()
        book1.score = -1
        author1 = Author.objects.get(id=0)
        book1.save()
        book1.author.add(author1)
        book1.path_to_cover_image = "1.jpg"
        book1.save()
        self.assertTrue(book1.score == 0)
        # Score maytor de 10
        book2 = Book()
        book2.id = 2
        book2.title = faker.name()
        book2.isbn = "1224" + str(book2.id)
        book2.price = faker.random_int(min=1, max=100)
        book2.number_copies_stock = faker.random_int(min=1, max=20)
        book2.date = faker.past_datetime()
        book2.score = 11
        author2 = Author.objects.get(id=2)

        book2.save()
        book2.author.add(author1)
        book2.path_to_cover_image = "1.jpg"
        book2.save()
        self.assertTrue(book2.score == 10)

    """ Test para comprobar vista del home page """
    def test_home_page(self):

        self.client = Client()
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    """ Test para comprobar vista del search page """
    def test_search_page(self):

        self.client = Client()
        response = self.client.get(reverse('search'))
        self.assertTemplateUsed(response, 'search.html')