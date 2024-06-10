from django.db.models.signals import post_save, pre_delete

from gyuser.models.base import User, Profile


def create_profile_on_user_create(sender, instance=None, **kwargs):
    if kwargs.get('created'):
        Profile.objects.get_or_create(user=instance)


post_save.connect(create_profile_on_user_create, sender=User)
