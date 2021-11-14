from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Model representing a profile.
    AUTOR: Santos Saenz
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.user.__str__()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    """
    Funcion que actualiza el perfil
    de un usuario determinado.
    AUTOR: Santos Saenz
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
