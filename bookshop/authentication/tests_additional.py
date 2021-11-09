import sys
from django.test import TestCase

from catalog.models import Book, Comment, Author
from authentication.models import Profile
from faker import Faker
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

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

    """ Test para comprobar que se crean los objetos profile correctamente """
    def test_profile(self):
        user = User.objects.get(id=101)
        profile = Profile.objects.filter(user__in = User.objects.filter(id=101))[0]
        profile.__str__()
        self.assertEquals(profile.user, user)

    """ Test para comprobar pantalla signup """
    def test_signup(self):
        """ Usuario sin registrar, por lo que podre comprobar signup """
        self.client = Client()
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')
