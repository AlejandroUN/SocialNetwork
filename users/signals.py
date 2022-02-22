from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#When a User is created send a signal (that's why he's the sender)
#in this case is to create a Profile when we create a new User
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

#Now, when the useer is saved, save the profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	#Instance is the user
	instance.profile.save()