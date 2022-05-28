from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import Group, User
from intern_manager.models import UserProfile


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created,**kwargs):

    if created:
        UserProfile.objects.create(user=instance)

        
        

   