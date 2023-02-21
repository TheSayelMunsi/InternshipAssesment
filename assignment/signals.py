
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import client_table


@receiver(post_save, sender=User)
def create_user_picks(sender, instance, created, **kwargs):
    if created:
        client_table.objects.create(user=instance,name=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#         instance.client_table.save()