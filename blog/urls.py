from django.urls import path
from . import views


urlpatterns = [
	#now we have url path for our blog-home page mapped to our home function in our views file
    path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
]