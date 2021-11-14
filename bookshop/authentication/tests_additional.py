from django.test import TestCase
from authentication.models import Profile
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

    def test_profile(self):
        """
        Test para comprobar que se crean los objetos profile correctamente
        AUTOR: Carolina Monedero
        """
        user = User.objects.get(id=101)
        profile = Profile.objects.filter(user__in=User.objects.filter(id=101))[0] # noqa
        profile.__str__()
        self.assertEquals(profile.user, user)

    def test_signup(self):
        """
        Test para comprobar pantalla signup
        AUTOR: Carolina Monedero
        """
        self.client = Client()
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')
