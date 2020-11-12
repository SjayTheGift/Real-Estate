from django.urls import path
from .views import HomeView, about, search

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', about, name="about"),
    path('search/', search, name='search')
]
