from django.urls import path
from .views import GameListView,ListingListView,CreateListingView,MyListingsView

urlpatterns = [
    path('games/',GameListView.as_view(), name='game-list'),
    path('listings/',ListingListView.as_view(), name='listing-list'),
    path('create-listing/',CreateListingView.as_view(), name='create-listing'),
    path('my-listings/',MyListingsView.as_view(), name='my-listings'),
]