from django.urls import path
from .views import ListingView, ListingDetailView, contact

urlpatterns = [
    path('listings/', ListingView.as_view(), name="listings"),
    path('listings/<int:pk>/', ListingDetailView.as_view(), name="listing_detail"),
    path('contact/', contact, name="contact"),
]
