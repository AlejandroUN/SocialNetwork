from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#We'll use this to require to someone to be loged in before accessing to a page, like a profile for example
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
	#django already provides a user creation form
	#if we get a POST (that is when the user click the sign up button) request we'll try to validate the data from de form
	#if we get a GET (that is when the user loads the page) request we just show the blank form
	if request.method == 'POST':
		#Here we create a form with the data that was within that post request
		form = UserRegisterForm(request.POST)		
		#if the data is valid take the username
		if form.is_valid():			
			#This line below saves the user
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! Now you are able to log in')
			#form.save()
			return redirect('login')
		#flash message will just appear once
	else:
		print('invalid')
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

#The line below, is something called a decorator
#It as functionality to an existing function
#In this case we'll use it to require someone to be loged in before accessing to a page, like a profile for example
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')			
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)

