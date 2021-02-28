from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search_page'),
    path('about/', views.about, name='about_page'),
    path('download/', views.download, name='download_page'),
    # path('download/', views.download, name='download_page'),
]