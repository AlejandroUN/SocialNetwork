from django.urls import path
from .views import (PostListView, 
PostDetailView, 
PostCreateView,
PostUpdateView,
PostDeleteView)
from . import views


urlpatterns = [
	#now we have url path for our blog-home page mapped to our home function in our views file
	#That .as_view() is to load it as a view because we're calling a funciton base view, not a normal view
	path('', PostListView.as_view(), name='blog-home'),
    #path('', views.home, name='blog-home'),
	#that <int:pk> is for put a variable in a route, in this case
	#the primary key (that's an integer) of the post
	#that allow us to use that variable and use it in our PostDetailView
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('about/', views.about, name='blog-about'),

]