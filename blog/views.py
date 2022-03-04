# Create your views here.

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView)
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

#Function based views. a URL pattern are directed to these functions

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

#To our 
class PostListView(ListView):
	#Line below will tell django what model to query
	model = Post	
	#By default, class base views look for a template to put the info
	#in the direction <app>/<model>_<viewtype>.html in the templates folder
	template_name = 'blog/home.html'
	#Still we have to set the name of the variable that the template we'll be looping over
	#because the template we've defined look for variable called posts
	#and the name by the default of the variable that django uses is other called object_list or something similar
	context_object_name = 'posts'
	#now if we want to order our psots to see the newest at top we just declare another variable
	ordering = ['-date_posted']


class PostDetailView(DetailView):	
	#In this case, we're trying to do everything in default as django expects
	#That's why we created a template with the name that it expects instead of declaring a variable
	#and we basically copy the home.html template but with some changes
	model = Post		

#with the LoginRequiredMixin parameter, when trying to acces this function
#Django validates that the user is logged
class PostCreateView(LoginRequiredMixin, CreateView):		
	model = Post
	#The only other thing we need to provide are the fields that we'll need to provide to the form 
	#for creating a post
	fields = ['title', 'content']
	#To create django doesn't expect a post_create.html but a post_form.html

	#We're overriding this method so that we define the author and not the user typing it in the form
	def form_valid(self, form):
		#Since the author is something the user shouldnt be able to change when creating a post
		#we're putting the current user in the variable author of the instance
		form.instance.author = self.request.user
		return super().form_valid(form)
#The UserPassesTestMixin parameter is to validate that if a post will be updated
#it has to be updated only for the author of the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):		
	model = Post	
	fields = ['title', 'content']
	#Update will also use the post_form.html template
	
	def form_valid(self, form):		
		form.instance.author = self.request.user
		return super().form_valid(form)

	#UserPassesTestMixin  just validate if a user passes a test condition
	#so we'll declare that test to be that the user that tries to update a post be the author of that post
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = Post
	#We add a succes url to redirect the user when the post is deleted
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False	

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})

#There are function base views: List views, detaile, create views, update views,  delete views, etc



