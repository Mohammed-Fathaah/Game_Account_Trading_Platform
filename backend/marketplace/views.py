from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Game,AccountListing
from .serializers import GameSerializer,AccountListingSerializer

#List all games
class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

#Seller creates Listing
class CreateListingView(generics.CreateAPIView):
    queryset = AccountListing.objects.all()
    serializer_class = AccountListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

#Buyer views all listings
class ListingListView(generics.ListAPIView):
    queryset = AccountListing.objects.filter(status='available')
    serializer_class = AccountListingSerializer
    