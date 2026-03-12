from rest_framework import serializers
from .models import Game,AccountListing

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Game
        fields='__all__'

class AccountListingSerializer(serializers.ModelSerializer):
    seller=serializers.ReadOnlyField(source='seller.usernmae')

    class Meta:
        model=AccountListing
        fields='__all__'