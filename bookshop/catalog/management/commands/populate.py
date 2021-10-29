# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate
#
# use module Faker generator to generate data (https://zetcode.com/python/faker/)
import os

from django.core.management.base import BaseCommand
from catalog.models import (Author, Book, Comment)
from django.contrib.auth.models import User
from faker import Faker
from decimal import Decimal
# define STATIC_PATH in settings.py
from bookshop.settings import STATIC_PATH
from PIL import Image, ImageDraw, ImageFont


FONTDIR = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#

faker = Faker()

class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    # def add_arguments(self, parser):

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here
        if 'DYNO' in os.environ:
            self.font = \
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
        else:
            self.font = \
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf"


        self.NUMBERUSERS = 20
        self.NUMBERBOOKS = 30
        self.NUMBERAUTHORS = 5
        self.MAXAUTHORSPERBOOK = 3
        self.NUMBERCOMMENTS = self.NUMBERBOOKS * 5
        self.MAXCOPIESSTOCK = 30
        self.cleanDataBase()   # clean database
        # The faker.Faker() creates and initializes a faker generator,
        self.faker = Faker()
        self.user()
        self.author()
        self.book()
        self.comment()
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here

    def cleanDataBase(self):
        User.objects.all().delete()
        Author.objects.all().delete()
        Book.objects.all().delete()
        Comment.objects.all().delete()


    def user(self):
        id = 100
        for i in range (self.NUMBERUSERS):
            user = User(id=id+i,username=faker.name(),
                        password=faker.password())
            user.save()


    def author(self):
        for i in range (self.NUMBERAUTHORS):
            author = Author()
            author.id = i
            author.first_name = faker.first_name()
            author.last_name = faker.last_name()
            author.save()


    def cover(self, book):
        """create fake cover image.
           This function creates a very basic cover
           that show (partially),
           the primary key, title and author name"""

        img = Image.new('RGB', (200, 300), color=(73, 109, 137))
        # your font directory may be different
        fnt = ImageFont.truetype(
            self.font,
            28, encoding="unic")
        d = ImageDraw.Draw(img)
        d.text((10, 100), "PK %05d" % book.id, font=fnt, fill=(255, 255, 0))
        d.text((20, 150), book.title[:15], font=fnt, fill=(255, 255, 0))
        d.text((20, 200), "By %s" % str(
            book.author.all()[0])[:15], font=fnt, fill=(255, 255, 0))
        img.save(os.path.join(STATIC_PATH, book.path_to_cover_image))


    def book(self):
        isbn = 1000000000000
        for i in range (self.NUMBERBOOKS):
            book = Book()
            book.id = i
            book.title = faker.name()
            book.isbn = str(isbn + i)
            book.price = faker.random_int(min=1, max=100)
            book.number_copies_stock = faker.random_int(min=1, max=20)
            book.date = faker.past_datetime()
            book.score = faker.random_int(0, 10)
            book.author = [Author.objects.get(id=faker.random_int(0, self.NUMBERAUTHORS - 1))]
            book.path_to_cover_image = str(book.id)
            book.save()
            # Ultima
            Cover(book)


    def comment(self):
        for i in range (self.NUMBERCOMMENTS):
            comment.book = Book.objects.get(id=faker.random_int(0, self.NUMBERBOOKS - 1))
            comment.date = faker.past_datetime()
            comment.msg = faker.text()
            comment.user = faker
