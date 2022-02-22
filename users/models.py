from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
	#We're saying we'll define a one-to-one relationship between the user and profile model	
	#CASCADE means that if the user is deleted it will delete the profile, but not viceversa
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#All users have a default image, and the second parameter is where the pictures that users upload we'll be saved
	#For this we have to install Pillow to work with images
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	#Whenever we print a profile we'll be printed this way
	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			#Line below will resize the image
			img.thumbnail(output_size)
			img.save(self.image.path)


