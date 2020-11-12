from django.urls import path
from .views import Profile, change_password

urlpatterns = [
    path('accounts/profile/', Profile.as_view(), name="profile"),
    path('change-password/', change_password, name="change_password"),
]
