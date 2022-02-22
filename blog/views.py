# Create your views here.

from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse
#list of dictionaries
# posts = [
# 	{
# 		'author': 'Alejo',
# 		'title': 'Blog Post 1',
# 		'content': 'First post content',
# 		'date_posted': 'Fevrier 14, 2022'
# 	},
# 	{
# 		'author': 'CoreyMS',
# 		'title': 'Blog Post 2 ',
# 		'content': 'Second post content',
# 		'date_posted': 'Fevrier 14, 2022'
# 	}
# ]


#This is how we handle certain routes
def home(request):
	#context is a dictionary that has a key that will be accessible from our templates
	context = {
		#we'll pass the all the posts from our databases
		'posts': Post.objects.all()
	}
	#If we would load static content we would just pass two arguments to render() function
	#But, it's not just static content we will have to pass a third argument that's called context
	#This way the page we'll render will have access to that data
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})
