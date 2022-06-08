from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, UserDocument

user = settings.AUTH_USER_MODEL


@receiver(post_save, sender=user)
def create_profile(sender, **kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])


@receiver(post_save, sender=user)
def create_docs(sender, **kwargs):
    if kwargs["created"]:
        UserDocument.objects.create(user=kwargs["instance"])
