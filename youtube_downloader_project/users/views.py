from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile


def register(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.data.get("username")
			password = form.data.get("password1")
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
			return redirect("login_page")

	return render(request, "users/register.html", {"form" : form})


def profile_page(request):
	profile = Profile.objects.get(id=request.user.id)
	return render(request, "users/profile.html", {"profile" : profile})