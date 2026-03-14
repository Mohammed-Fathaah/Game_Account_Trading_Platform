from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Game,AccountListing
from .serializers import GameSerializer,AccountListingSerializer

class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CreateListingView(generics.CreateAPIView):
    queryset = AccountListing.objects.all()
    serializer_class = AccountListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ListingListView(generics.ListAPIView):
    queryset = AccountListing.objects.filter(status='available')
    serializer_class = AccountListingSerializer

class MyListingsView(generics.ListAPIView):
    serializer_class = AccountListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AccountListing.objects.filter(seller=self.request.user)
    