from django.db import models
from django.utils import timezone
#posts and users we'll be related
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	#inside goes the attributes of our model

	#what goes inside are constraints or restrictions
	title = models.CharField(max_length=100)
	content = models.TextField()
	#we didn't do timezone.now() because we don't want oto activate now, just until someone creates a post
	date_posted = models.DateTimeField(default=timezone.now)
	#We define a foreign key from user
	#on_delete we say thath if the user is deleted the post will be deleted too
	#But if we delete the post, the user won't be deleted
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	#This will format better this a post object when we print it
	def __str__(self):
		return self.title