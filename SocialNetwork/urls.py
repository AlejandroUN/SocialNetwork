"""SocialNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
#another way to declare a url pattern for an app
from users import views as user_views

#Map url's to certain locations so that we can handle them in a certain way

urlpatterns = [
    path('admin/', admin.site.urls),
	#Now when we open our web page to the browser and go to /blog it will map that to our blog url's :0
	path('', include('blog.urls')),
	#If we would want that the home of one of our applications
	#were the home of the hole project we would simply do
	#something as follows
	#path('', include('blog.urls')),
	#another way to declare a url pattern for an app
	path('register/', user_views.register, name='register'),
	path('profile/', user_views.profile, name='profile'),
	#we'll use django default login, we have to add the next to lines
	#template_name='users/login.html' is to tell django that ook the template for that route in that path
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),	
]

#Setings is thing we imported, that means that fi we're in debug mode 
#then we want to add those url patterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
