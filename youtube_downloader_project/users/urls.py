from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register_page"),
    path('profile/', views.profile_page, name="profile_page"),
	path('login/', auth_views.LoginView.as_view(), name='login_page'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout_page'),
]
