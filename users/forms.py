#We create a form that inherites from django users default form 

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	#And now we add the fields we want to add to add to the form
	#If we would want to leave this field optional we put inside the parenthesis a false
	email = forms.EmailField()

	#Inside here we're gonna put the model we want the form to interact with
	#We say the model we'll be affected is a user model	
	class Meta:
		model = User
		#The fields we'll show and in that order
		fields = ['username', 'email', 'password1', 'password2']


#We're gonna create a model form, a form thath works with a specific model
#in this case our User model
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = User		
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']